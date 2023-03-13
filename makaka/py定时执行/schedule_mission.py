'''
Execute function every once in a while
'''
import schedule
import time

def job(message1, message2):
    print(message1, message2)
    
schedule.every(3).seconds.do(lambda: job("hello", "world"))
# schedule.every(10).minutes.do(job)        # 10分钟一次
# schedule.every().hour.do(job)             # 1小时一次
# schedule.every().day.at("10:30").do(job)   # 每天10:30一次
# schedule.every().monday.do(job)            # 每周一的这个时候一次
# schedule.every().wednesday.at("13:15").do(job) # 每周三13:15一次
# schedule.every().minute.at(":17").do(job)      # 每分钟的第17秒一次

while True:
    schedule.run_pending()
    time.sleep(1)