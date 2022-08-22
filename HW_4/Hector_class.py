class Hectors:
    def __init__(self, *args):
        self.__data = 5000 * [None]
        self.__values = args
       
        # args to list
        index = 0
        for element in self.__values:
            self.__data[index] = element
            index += 1

        self.__len = index

    def length(self):
        return self.__len

    def add_element(self, *args):
        for element in args:
            self.__data[self.__len] = element
            self.__len += 1

    def show(self):
        print("|<", end="")
        for i in range(self.__len):
            print(self.__data[i], end="")
            if i+1 != self.__len:
                print(", ", end="")
        print(">|")

    def delete_element(self, index=5001):
        if index < self.__len:
            for j in range (index, self.__len):
                pass
        else:
            print("Index out of range")
            

x = Hectors(456,464,456, "asdfasd")
print(x.length())
x.add_element("sdfgs")
x.show()
x.delete_element(3)
print(x.length())
