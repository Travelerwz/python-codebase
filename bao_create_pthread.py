#!/usr/bin/python3
#引入线程包
import _thread
import time

#创建线程函数
def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s:%s" % (threadName,time.ctime(time.time())))
#创建线程函数
try:
    _thread.start_new_thread(print_time,("thread_1",2, ))
    _thread.start_new_thread(print_time,("thread_2",4, ))
except:
    print("error:create thread error")

while 1:
    pass
