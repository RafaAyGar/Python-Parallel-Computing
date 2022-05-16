from time import sleep
from threading import Thread, Condition

class StingySpendy:
    money = 100
    cv = Condition()

    def Stingy(self):
        for i in range(10000):
            self.cv.acquire()
            self.money += 10
            self.cv.notify()
            self.cv.release()
        print("Stingy Done!")

    def Spendy(self):
        for i in range(7000):
            self.cv.acquire()
            while self.money < 20:
                self.cv.wait()
            self.money -= 20
            self.cv.release()
        print("Spendy Done!")

def main():
    ss = StingySpendy()
    t1 = Thread(target=ss.Stingy(), args=())
    t2 = Thread(target=ss.Spendy(), args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print("Money:", ss.money)

main()