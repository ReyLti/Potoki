from RandomWordGenerator import RandomWord
from multiprocessing import Process
import multiprocessing
from random import randint
from threading import Thread
import os


def create():
    file = open (str(os.getpid())+".txt","a")
    x=0
    while x <randint(100,500):
        rw = RandomWord(max_word_size=randint(1,10))
        file.write(rw.generate()+"\n")
        x=x+1
    file.close()

if __name__ == "__main__":
    print("Start")
    for i in range(1,multiprocessing.cpu_count()+1):
        prol = Process(target=create)
        prol.start();
        prol.join()
        
