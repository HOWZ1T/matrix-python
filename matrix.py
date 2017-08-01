#Created by Dylan Randall
#Created: 20/03/2017
import random

class Matrix:
    xy = []
    order = []
    def __init__(self, rows, columns):
        self.order = [rows, columns]
        self.xy = [[0 for i in range(columns)] for j in range(rows)]

    def setRow(self, row, values):
        for column in range(self.order[1]):
            self.xy[row][column] = values[column]

    def setColumn(self, column, values):
        for row in range(self.order[1]):
            self.xy[row][column] = values[row]

    def set(self, values): #values are done row first i.e: if we have 3 columns and 2 rows = [[0,1,2] , [3,4,5]] where 012 is the first row and 345 is the second row #Values must be in a list of rows
        vLen = len(values) #values length

        valid = True #valid input
        if vLen != self.order[0]:
            valid = False
        else:
            for row in values:
                if len(row) != self.order[1]:
                    valid = False
                    continue

        if valid == False:
            print("Error in setting matrix! Invalid input!")
        else:
            rCounter = 0 #rowCounter
            cCounter = 0 #columnCounter
            for row in values:
                cCounter = 0
                for column in row:
                    self.xy[rCounter][cCounter] = column
                    cCounter += 1
                rCounter += 1
            #garbage collection    
            del rCounter
            del cCounter
        del valid
        del vLen
        
    def setElement(self, row, column, value):
        try:
            self.xy[row][column] = value
        except IndexError:
            print("Matrix could not enter element at position: "+str(row)+":"+str(column)+" as the index is out of bounds!")
        
    def getElement(self, row, column):
        try:
            return self.xy[row][column]
        except IndexError:
            print("Could not return element at position: "+str(row)+":"+str(column)+" as the index is out of bounds!")

    def print(self):
        print("Matrix:\n")
        for row in self.xy:
            print(row)
            
    def getOrder(self):
        return self.order

    def getXY(self):
        return self.xy

    def randomFill(self, seed, minValue, maxValue): #randomly fills the matrix with random values.
        if minValue == '': #defaults the min, max values if they are not given
            minValue = -100

        if maxValue == '':
            maxValue = 100
            
        s = seed
        maxValue += 1#as the random.randrange function excludes the max value i.e  a max value of 100 will have a true max of 99, thus incrementing the max value by 1 solves the problem
        for row in range(self.order[0]):
            for column in range(self.order[1]):
                random.seed(s)
                s += 1 #increments the seed to produce randomness in the totallity of the matrix whilst still providing reproducability.
                self.setElement(row, column, random.randrange(minValue, maxValue))
        del s #garbage collection
        del minValue
        del maxValue

    def randomGraph(self, seed, maxValue): #generates a random matrix that can be used for weighted and unweighted graphs, however it is not a true graph matrix
        if maxValue == None:
            print("Error no max value supplied !")
            return None
            
        s = seed
        maxValue += 1
        for row in range(self.order[0]):
            for column in range(self.order[1]):
                random.seed(s)
                s += 1 #increments the seed to produce randomness in the totallity of the matrix whilst still providing reproducability.
                self.setElement(row, column, random.randrange(0, maxValue)) #the greater the max value the less likely 0's are to occur and vice versa

        del s #garbage collection
        del maxValue

    def __add__(self, other):#+ addition of matrices
        oA = self.getOrder() #orderA
        oB = other.getOrder() #orderB
        if oA[0] == oB[0] and oA[1] == oB[1]: #if orders of the matrix's are equal
            m = Matrix(oA[0], oA[1])
            for row in range(oA[0]):
                for column in range(oA[1]):
                    m.setElement(row, column, (self.getElement(row, column)+other.getElement(row, column)))

            return m
        else:
            print("Cannot add the matrices, their orders do not match!")
            return None

    def __sub__(self, other):#- subtraction of matrices
        oA = self.getOrder() #orderA
        oB = other.getOrder() #orderB
        if oA[0] == oB[0] and oA[1] == oB[1]: #if orders of the matrix's are equal
            m = Matrix(oA[0], oA[1])
            for row in range(oA[0]):
                for column in range(oA[1]):
                    m.setElement(row, column, (self.getElement(row, column)-other.getElement(row, column)))

            return m
        else:
            print("Cannot subtract the matrices, their orders do not match!")
            return None

    def __mul__(self, other):#* multiplication of matrices
        oA = self.getOrder()
        oB = other.getOrder()
        if oA == oB:
            m = Matrix(oA[0], oB[1])

            for rowA in range(oA[0]):
                for columnB in range(oB[1]):
                    val = 0
                    for columnA in range(oA[1]):
                        val += self.getElement(rowA, columnA)*other.getElement(columnA, columnB)
                    m.setElement(rowA, columnB, val)

            return m
        else:
            print("Cannot multiply matrices, their orders do not match!")
            return None
        
    def __rmul__(self, other):#* reverse multiplication of matrices
        oA = self.getOrder()
        oB = other.getOrder()
        if oA == oB:
            m = Matrix(oA[0], oB[1])

            for rowA in range(oA[0]):
                for columnB in range(oB[1]):
                    val = 0
                    for columnA in range(oA[1]):
                        val += self.getElement(rowA, columnA)*other.getElement(columnA, columnB)
                    m.setElement(rowA, columnB, val)

            return m
        else:
            print("Cannot multiply matrices, their orders do not match!")
            return None
        
    def __lt__(self, other): #< #scalar []*2,  scalar muliplication of matrix
        order = self.getOrder()
        m = Matrix(order[0], order[1])

        for row in range(order[0]):
            for column in range(order[1]):
                m.setElement(row, column, (self.getElement(row, column)*other))

        return m

    def __gt__(self, other):#> #scalar 2*[], scalar muliplication of matrix
        order = other.getOrder()
        m = Matrix(order[0], order[1])

        for row in range(order[0]):
            for column in range(order[1]):
                m.setElement(row, column, (other.getElement(row, column)*self))

        return m

    def __invert__(self):#~ #transpose of matrix
        order = self.getOrder()
        m = Matrix(order[1], order[0])

        for row in range(order[0]):
            for column in range(order[1]):
                m.setElement(column, row, self.getElement(row, column))

        return m

    def __xor__(self, other):#^ #pow, multiplies the matrix to the power
        order = self.getOrder()
            
        if order[0] != order[1]:
            print("Matrices need to be square i.e: square matrices can only be raised to a power!")
            return
        orgS = self
        for i in range(other-1):
            self = self*orgS

        return self

    def __eq__(self, other):#==, determines if two matrices are equal to each other or not.
        oA = self.getOrder()
        oB = other.getOrder()
        if oA[0] != oB[0] or oA[1] != oB[1]:
            return False
        else:
            for row in range(oA[0]):
                for column in range(oA[1]):
                    eA = self.getElement(row, column)
                    eB = other.getElement(row, column)

                    if eA != eB:
                        return False

            return True

#Created by Dylan Randall
