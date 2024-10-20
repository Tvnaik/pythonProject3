from multipledispatch import dispatch

@dispatch(int,int)
def disp(val1,val2):
    print("The  int numbers are:",val1,"\t",val2)

@dispatch(int,int,int)
def disp(val1,val2,val3):
    print("The three num are: ",val1," ",val2," ",val3)

@dispatch(str)
def disp(val):
    print("Hello",val)

disp(12,34)
disp(1,5,2)
disp("Tushar")


