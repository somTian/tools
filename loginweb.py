import requests
import schedule
import datetime
import time

def login_web():

    #设置登录网址
    url = 'http://172.16.200.13'

    #设置账号密码
    data = [
        ('DDDDD', '帐号'),
        ('upass', '密码'),
        ('0MKKey', ''),
    ]


    print("当前时间为：", datetime.datetime.now())
    res = requests.post(url, data=data)
    print(res)

def sche_run():
    schedule.clear()

    schedule.every(10).seconds.do(login_web)

    # schedule.every().day.at("8:00").do(login_web)
    # schedule.every().day.at("10:00").do(login_web)
    # schedule.every().day.at("14:00").do(login_web)
    # schedule.every().day.at("16:00").do(login_web)
    # schedule.every().day.at("18:00").do(login_web)
    # schedule.every().day.at("20:00").do(login_web)

    #设置定时任务
    # schedule.every(10).minutes.do(job)  # 每隔 10 分钟运行一次 job 函数
    # schedule.every().hour.do(job)  # 每隔 1 小时运行一次 job 函数
    # schedule.every().day.at("10:30").do(job)  # 每天在 10:30 时间点运行 job 函数
    # schedule.every().monday.do(job)  # 每周一 运行一次 job 函数
    # schedule.every().wednesday.at("13:15").do(job)  # 每周三 13：15 时间点运行 job 函数
    # schedule.every().minute.at(":17").do(job)  # 每分钟的 17 秒时间点运行 job 函数

    while True:
        schedule.run_pending()  # 运行所有可以运行的任务
        time.sleep(1)

if __name__ == "__main__":

    sche_run()
