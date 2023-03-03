# 小马的代码仓库

本项目包含常见的代码片段，使得开发时不用再去找各种散乱的信息。

### linux常见命令

```
alias bt=bluetoothctl  # 重命名，将bluetoothctl命名为bt
watch bluetoothctl list  # 循环跑指令，默认两秒一次
dmesg  -w   # 打出系统log,且等待
lsusb     # 列出当前usb设备
journalctl -u  

```

### 树莓派引脚操作

![rpi-pins-40-0](https://shumeipai.nxez.com/wp-content/uploads/2015/03/rpi-pins-40-0.png)

总共有3种模式，即

```
GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
```

引脚操作是相通的。
