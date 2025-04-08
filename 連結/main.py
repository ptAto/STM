import GUI
import data
import os
import threading
import time
tine=None
def timee():
    while True:
        tine=int(time.time())
        print(tine)
        time.sleep(1)

start_time=time.time

thread_GUI=threading.Thread(target=GUI.GUI)
thread_time=threading.Thread(target=timee)
thread_data=threading.Thread(target=data.data)
thread_data.start()
thread_GUI.start()
thread_time.start()

end_time=time.time