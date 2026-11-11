def get_name():
    while True:
        name= input("enter name")
        if name:
            return name
def get_num():
    while True:
        try:
           num = int(input("enter number"))
           if 10 < num >0 and isinstance(num,int):
               return num
        except ValueError as e:
            print (f"{e} you have mistake")
print(get_num())
