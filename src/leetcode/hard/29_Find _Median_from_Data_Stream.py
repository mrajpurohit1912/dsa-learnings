class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()

        n = len(self.data)

        if n % 2 == 1:
            return self.data[n//2]
            
        else:
            middle_left = self.data[n //2 -1] 
            middle_right = self.data[n //2 ]

            return  (middle_left + middle_right) / 2
            


if __name__ == "__main__":
    pass
