class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod  #=> this means this can only access class attributes
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")   


l1 = Laptop("16gb", "512gb")
l2 =Laptop("18gb", "256gb") 

l1.get_info()
l2.get_info()