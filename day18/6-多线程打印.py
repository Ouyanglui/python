# 作者：coding ur life
# 2022年06月20日22时12分18秒
from threading import Thread
import time
def say_hello():
    print('好饿啊')
    time.sleep(1)
if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=say_hello)
        t.start()
