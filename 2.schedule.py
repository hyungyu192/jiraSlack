#/usr/bin/python3
# 참고할만한 레퍼런스는 아래를 참고 하길 바래요!
# schedule https://buildmedia.readthedocs.org/media/pdf/schedule/stable/schedule.pdf 
# Process https://docs.python.org/2/library/multiprocessing.html
# schedule jobs parallel https://schedule.readthedocs.io/en/stable/faq.html#how-to-execute-jobs-in-parallel
# multiprocess https://niceman.tistory.com/145?category=940952



import schedule
import time

def job():
    print("I'm working...")


schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)