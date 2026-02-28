class BankAccount:
    def __init__(self, name, balance, cast):
        self.name = name #public
        self._cast = cast #protected
        self.__balance = balance  #private => data mangling

    def  get_balance(self):  #getter
        return self.__balance    
    
    def  set_balance(self, newBalance):  #setter
        self.__balance = newBalance 


acc1 = BankAccount("Pawan chauhan", 100_000, "chauhan")

acc1.set_balance(90_000)
print(acc1.name, acc1.get_balance())        