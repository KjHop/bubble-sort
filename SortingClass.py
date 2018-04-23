class Sorting:

    listOfNumbers = []

    def addNumber(self,number):
        self.listOfNumbers.append(number)

    def printList(self):
        print(self.listOfNumbers)

    def printEachElementOfList(self):
        for number in self.listOfNumbers:
            print(number)

    def bubbleSort(self):
        for i in range(len(self.listOfNumbers)-1, 0, -1):
            for j in range(i):
                if self.listOfNumbers[j] > self.listOfNumbers[j+1]:
                    #Change positions of list values
                    self.listOfNumbers[j], self.listOfNumbers[j+1] = self.listOfNumbers[j+1], self.listOfNumbers[j]
        return self.listOfNumbers