import time
import math

import os
import serial
import threading

from config import config_class
from event import EventRunner, Enum, Event
from logger import log


class RadioButtonEventType(Enum):
    CLICK = 'click'


class RadioButtonEvent(Event):
    """An event from radio button with button id attached"""

    def __init__(self, event_type: Enum, button_id: int):
        super(RadioButtonEvent, self).__init__(event_type=event_type)
        self.button_id = button_id


@config_class
class RadioButtonHub:

    dev_dir: str = '/dev'
    dev_prefix: str = 'ttyUSB'
    dev_search_interval: float = 1.0
    baud_rate: int = 9600
    msg_len: int = 13
    msg_id_char: int = 8

    def __init__(self):
        self.ser = serial.Serial(baudrate=self.baud_rate)
        self.event_runner = EventRunner(RadioButtonEventType)
        self._main_thread = threading.Thread(target=self._main, daemon=True)
        self._main_thread.start()

    def _main(self):
        while True:
            if not self.ser.is_open:
                self._update_device()
            try:
                data = self.ser.readline()
            except serial.SerialException:
                log.warning('serial exception when reading; disconnection?')
                self.ser.close()
                self.ser.port = None
                continue
            if len(data) != self.msg_len:
                log.warning(f'incorrect data length {len(data)} for {data}')
                continue
            log.debug(f'data line read from radio = {data}')
            msg = data.decode('ascii')
            id_char = msg[self.msg_id_char]
            if id_char not in ('1', '2', '4', '8'):
                log.error(f'illegal id char "{id_char}"')
                continue
            btn_id = int(math.log2(int(id_char)))
            log.debug(f'radio button pressed at #{btn_id}')
            self.event_runner.trigger(
                RadioButtonEvent(RadioButtonEventType.CLICK, button_id=btn_id))

    def _update_device(self):
        log.debug(f'searching for {self.dev_dir}/{self.dev_prefix}*')
        while True:
            dev_paths = [d for d in os.listdir(self.dev_dir)
                         if str(d).startswith(self.dev_prefix)]
            if not dev_paths:
                time.sleep(self.dev_search_interval)
                continue
            if len(dev_paths) > 1:
                log.warning(f'multiple radio devices: {dev_paths}; using 1st')
            port = f'{self.dev_dir}/{dev_paths[0]}'
            self.ser.port = port
            try:
                self.ser.open()
            except serial.SerialException:
                log.error(f'error opening serial port {port}')
                time.sleep(self.dev_search_interval)
                continue
            log.info(f'radio serial port opened at {self.ser.port}')
            break

    def clean_up(self):
        self.ser.close()
