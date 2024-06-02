import time

class StopWatch:
    def __init__(self):
        self.__startTime = time.time()
        self.__endTime = time.time()
    
    def start(self):
        self.__startTime = time.time()
    
    def stop(self):
        self.__endTime = time.time()
    
    def getElapsedTime(self):
        return self.__endTime - self.__startTime
    
    def getStartTime(self):
        return self.__startTime
    
    def getEndTime(self):
        return self.__endTime

def main():
    stopwatch = StopWatch()
    stopwatch.start()
    
    sum = 0
    for i in range(1000000):
        sum += i
    
    stopwatch.stop()
    
    print("The elapsed time is", stopwatch.getElapsedTime(), "seconds")
    print("Total sum:", sum)

main()
