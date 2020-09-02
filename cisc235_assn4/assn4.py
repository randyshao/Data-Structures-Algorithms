
import math

class HashTable:

    def __init__(self, size):

        self.size = size
        self.table = [None] * self.size
        self.keyCount = 0
        self.comparisons = 0
        self.c1 = 0.875
        self.c2 = 1.625
        self.sumInsertLength = 0
        self.insertKeyNum = 0
        self.averageSearchLength = 0
        self.maxInsertLen = 0

    def QPhashFunction(self, keyVal):

        constant = 0.61803398875
        productKey = keyVal * constant
        productKeyInt = int(productKey)
        num = productKey - productKeyInt
        probe = int(num * self.size)
        return probe

    def DHhashFunction1(self, keyVal):

        constant = 0.61803398875
        productKey = keyVal * constant
        productKeyInt = int(productKey)
        num = productKey - productKeyInt
        probe = int(num * self.size)
        return probe

    def DHhashFunction2(self, keyVal):

        x = math.log(keyVal) / (math.log(2)) * 0.61803398875
        y = x - int(x)
        output = int(self.size * y)

        exponent = math.log(self.size) / math.log(2)

        if exponent % 1 == 0:
            if output % 2 == 1:
                return output
            elif output == self.size - 1:
                return output - 1
            else:
                return output + 1
        return output

    def conversion(self, keyName):
        numbers = []
        for letter in keyName:
            number = ord(letter) - 96
            numbers.append(number)
        keyVal = ""
        for i in numbers:
            keyVal += (str(i))
        return int(keyVal)

    def QPavgSearchLength(self, setData):

        success = False
        for d in range(2, 6):
            while success is False:
                try:
                    for keyName in setData:
                        keyVal = self.conversion(keyName)
                        self.QPinsert(keyVal, keyName)
                except IndexError:
                    print(keyName)
                    print("New size: ", self.size)
                    self.size += 10
                    self.table = [None] * self.size
                    continue

        self.averageSearchLength = self.sumInsertLength / self.insertKeyNum

        if self.averageSearchLength <= d:
            success = True
            print("The smallest table size to reach an average search length less than", d, "is ", self.size)
            print("The max search sequence length for the table is", self.maxInsertLen)
            print("The average search sequence length for the table is", self.averageSearchLength)
        else:
            self.size += 1
        success = False
        self.size = 2301

    def DHavgSearchLength(self, setData):

        success = False
        for d in range(2, 6):
            while success is False:
                try:
                    for keyName in setData:
                        keyVal = self.conversion(keyName)
                        self.QPinsert(keyVal, keyName)
                except:
                    self.size += 1
                    self.table = [None] * self.size
                    continue

                self.averageSearchLength = self.sumInsertLength / self.insertKeyNum

                if self.averageSearchLength <= d:
                    success = True
                    print("The smallest table size to reach an average search length less than", d, "is ", self.size)
                    print("The max search sequence length for the table is", self.maxInsertLen)
                else:
                    self.size += 1
            success = False
            self.size = 2301


    def QPinsert(self, keyVal, keyName):
        i = 0
        v = self.QPhashFunction(keyVal)
        # currentInsertLength = 0
        while i < self.size:
            a = int(v + (self.c1 * i) + (self.c2 ** i) % self.size)
        #    currentInsertLength += 1
            self.sumInsertLength += 1
            print("Insert length:", self.sumInsertLength)
            if self.table[a] == keyName:
                print("Attempt to insert duplicate key")
                break
            elif self.table[a] is None:
                self.table[a] = keyName
                print(keyName)
                print("index:", a)
                print(self.table)
                self.insertKeyNum += 1
                print("# of Keys inserted: ", self.insertKeyNum)
                break
            else:
                print(a, "is taken for", keyName)
                print("finding another spot")
                i += 1

        if i == self.size:
            print("Table Full")
            return -1

        # if currentInsertLength > self.maxInsertLen:
        #    self.maxInsertLen = currentInsertLength


    def DHinsert(self, keyVal, keyName):
        i = 0
        v1 = self.DHhashFunction1(keyVal)
        v2 = self.DHhashFunction2(keyVal)
        #currentInsertLength = 0
        while i < self.size:
            a = int(v1 + (i * v2) % self.size)
        #    currentInsertLength += 1
            self.sumInsertLength += 1
            if self.table[a] == keyName:
                print("Attempt to insert duplicate key")
                break
            elif self.table[a] is None:
                self.table[a] = keyName
                self.insertKeyNum += 1
                break
            else:
                i += 1

        if i == self.size:
            print("Table Full")
            return -1

        #if currentInsertLength > self.maxInsertLen:
        #    self.maxInsertLen = currentInsertLength

    def QPsearch(self, keyVal, keyName):
        i = 0
        v = self.QPhashFunction(keyVal)
        while i < self.size:
            a = (v + (self.c1 * i) + (self.c2 ** i) % self.size)
            if self.table[a] == keyName:
                print("Found it")
                break
            elif self.table[a] == None:
                print("Search value not found")
                break
            else:
                i += 1

        if i == self.size:
            print("Search value not found")
            return -1

    def DHsearch(self, keyVal, keyName):
        i = 0
        v1 = self.DHhashFunction1(keyVal)
        v2 = self.DHhashFunction2(keyVal)
        while i < self.size:
            a = int(v1 + (i * v2) % self.size)
            if self.table[a] == keyName:
                print("Found it")
                break
            elif self.table[a] == None:
                print("Search value not found")
                break
            else:
                i += 1

        if i == self.size:
            print("Search value not found")
            return -1

def main():

    data = open("HOTNCU_project_names_2020.txt", "r")
    setData = []

    for i in data:
        setData.append(i[:-1])

    size = 2301
    hashQP = HashTable(size)
    hashQP.QPavgSearchLength(setData)
    hashDH = HashTable(size)
    hashDH.DHavgSearchLength(setData)

main()

'''
    def conversion(self, keyName):
        charList = list(keyName)
        print(charList)
        length = len(charList)
        intList = [200, 52, 8]
        sum = 0
        for i in range(len(charList)):
            sum += charList[i] * intList[i % 3]
            print(sum)
        return sum
        #stringKey = ""
        #for i in keyName:
        #    stringKey += str(ord(i))
        #keyVal = 19 - (int(stringKey) * 11) % 19
        #return keyVal
'''