from DistanceEstimation import x_new
from multiprocessing import Process, Queue

def turnRight(signal):
    if signal:
        print("Right")
        while signal:
            pass

def turnLeft(signal):
    if signal:
        print("Left")
        while signal:
            pass

def goStraight(signal):
    if signal:
        print("Straight")
        while signal:
            pass


while(1):
    if(x_new>10):
            turnRight(1)
            turnLeft(0)
            goStraight(0)


    elif(x_new<-10):
            turnRight(0)
            turnLeft(1)
            goStraight(0)

    else:
            turnRight(0)
            turnLeft(0)
            goStraight(1)