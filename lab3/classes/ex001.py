class MyString:
    def getString(self):
        self.txt = input("Enter a string: ")

    def printString(self):
        print(self.txt.upper())

p1=MyString()

p1.getString()
p1.printString()
