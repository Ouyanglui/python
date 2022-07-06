# 作者：coding ur life
# 2022年06月20日22时16分57秒
import threading
def while1():
    while True:
        pass
if __name__ == '__main__':
    t = threading.Thread(target=while1)
    t.start()
    while True:
        pass