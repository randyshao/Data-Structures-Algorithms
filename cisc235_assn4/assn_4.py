#Name: Randy Shao
#Student Number: 20100992

class HashTable:

    def __init__(self, size):

        self.size = size
        self.table = [None] * self.size
        self.c1 = 0.875
        self.c2 = 1.625
        self.averageSearchLength = 0
        self.seqList = []

    def conversion(self, keyName):
        numbers = []
        for letter in keyName:
            number = ord(letter) - 96
            numbers.append(number)
        keyVal = ""
        for i in numbers:
            keyVal += (str(i))
        return int(keyVal)

    def hashFunction2(self, keyName):

        key = ""
        for i in keyName:
            key += str(ord(i))

        keyVal = 17 - (int(key) * 11) % 17
        return keyVal

    def avgSearchLength(self):

        sum = 0
        for i in self.seqList:
            sum += len(i)

        sequence = len(self.seqList)

        self.averageSearchLength = sum / sequence

    def QPinsert(self, keyName):
        currentSeq = []
        i = 0
        v = self.conversion(keyName)
        while i < self.size:
            a = int((v + (self.c1*i) + (self.c2*(i ** 2))) % self.size)
            currentSeq.append(a)
            if self.table[a] == keyName:
                print("Attempt to insert duplicate key")
                break
            elif self.table[a] is None:
                self.table[a] = keyName
                self.seqList.append(currentSeq)
                break
            else:
                i += 1

        if i == self.size:
            print("Table Full")
            return

    def DHinsert(self, keyName):
        currentSeq = []
        i = 0
        v1 = self.conversion(keyName)
        v2 = self.hashFunction2(keyName)
        while i < self.size:
            a = int((v1 + (i * v2)) % self.size)
            currentSeq.append(a)
            if self.table[a] == keyName:
                print("Attempt to insert duplicate key")
                break
            elif self.table[a] is None:
                self.table[a] = keyName
                self.seqList.append(currentSeq)
                break
            else:
                i += 1

        if i == self.size:
            print("Table Full")
            return

    def QPsearch(self, keyName):
        i = 0
        v = self.conversion(keyName)
        while i < self.size:
            a = int((v + (self.c1 * i) + (self.c2 * (i ** 2))) % self.size)
            if self.table[a] == keyName:
                print("Found it")
                break
            elif self.table[a] is None:
                print("Search value not found")
                break
            else:
                i += 1

        if i == self.size:
            print("Search value not found")
            return -1

    def DHsearch(self, keyName):
        i = 0
        v1 = self.conversion(keyName)
        v2 = self.hashFunction2(keyName)
        while i < self.size:
            a = int((v1 + (i * v2)) % self.size)
            if self.table[a] == keyName:
                print("Found it")
                break
            elif self.table[a] is None:
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
    primeNumList = []

    for n in range(2300, 3000):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                primeNumList.append(n)

    for i in data:
        setData.append(i[:-1])

    for size in primeNumList:
        hashQP = HashTable(size)

        for keyName in setData:
            hashQP.QPinsert(keyName)
        hashQP.avgSearchLength()

        if hashQP.averageSearchLength > 4.96 and hashQP.averageSearchLength <= 5:
            print("QP Hashtable size (d < 2): ", hashQP.size)
            print("QP Average Search Length (d < 2): ", hashQP.averageSearchLength)
        elif hashQP.averageSearchLength > 3.95 and hashQP.averageSearchLength <= 4:
            print("QP Hashtable size (d < 3): ", hashQP.size)
            print("QP Average Search Length (d < 3): ", hashQP.averageSearchLength)
        elif hashQP.averageSearchLength > 2.99 and hashQP.averageSearchLength <= 3:
            print("QP Hashtable size (d < 4): ", hashQP.size)
            print("QP Average Search Length (d < 4): ", hashQP.averageSearchLength)
        elif hashQP.averageSearchLength > 1.95 and hashQP.averageSearchLength <= 2:
            print("QP Hashtable size (d < 5): ", hashQP.size)
            print("QP Average Search Length (d < 5): ", hashQP.averageSearchLength)

    for size in primeNumList:
        hashDH = HashTable(size)

        for keyName in setData:
            hashDH.DHinsert(keyName)
        hashDH.avgSearchLength()

        if hashDH.averageSearchLength > 4.84 and hashDH.averageSearchLength <= 5:
            print("DH Hashtable size (d < 2): ", hashDH.size)
            print("DH Average Search Length (d < 2): ", hashDH.averageSearchLength)
        elif hashDH.averageSearchLength > 3.97 and hashDH.averageSearchLength <= 4:
            print("DH Hashtable size (d < 3): ", hashDH.size)
            print("DH Average Search Length (d < 3): ", hashDH.averageSearchLength)
        elif hashDH.averageSearchLength > 2.909 and hashDH.averageSearchLength <= 3:
            print("DH Hashtable size (d < 4): ", hashDH.size)
            print("DH Average Search Length (d < 4): ", hashDH.averageSearchLength)
        elif hashDH.averageSearchLength > 1.99 and hashDH.averageSearchLength <= 2:
            print("DH Hashtable size (d < 5): ", hashDH.size)
            print("DH Average Search Length (d < 5): ", hashDH.averageSearchLength)
main()