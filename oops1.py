class demo:
    value=""
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        n = self.num1 + self.num2
        print(n)

    def fun(self):
        print(self.num1)
        print(self.num2)

    def gum(self):
        print(self.num1)
        print(self.num2)


def main():
    obj1 = demo(1,3)
    obj2 = demo(3,5)
    obj1.fun()
    obj2.fun()
    obj1.gum()
    obj2.gum()
    

if __name__ =="__main__":
    main()
    