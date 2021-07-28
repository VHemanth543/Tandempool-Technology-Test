print("Welcome to Calculator");

bool = True;

class Calculator :
    def add(self,a,b):
        c = a + b;
        return c;

    def sub(self, a,b):
        c = a - b;
        return  c;

    def mul(self, a , b):
        c = a * b;
        return c;
    def div(self , a ,b ):
        c = a / b;
        return c;





while(bool):
    print("Select the peration to be performed \n" );
    op = int(input("Enter 1 for addition \n Enter 2 for subtraction \n Enter 3 for multiplication \n Enter 4 for division \n Enter 5 to EXIT \n"));
    if op == 5:
        bool = False;
        break;
    a = int(input("Enter a value :\n"));
    b = int(input("Enter b value :\n"));
    
    calc = Calculator;
    if (op > 5):
        print("Not a valid input \n");

    elif op == 1:
        result = calc.add(calc,a,b);
        print( "result is : ", result );
    elif op == 2:
        result = calc.sub(calc,a, b);
        print("result is : ", result);
    elif op ==3 :
        result = calc.mul(calc,a, b);
        print("result is : ", result);
    elif op == 4 :
        result = calc.div(calc,a, b);
        print("result is : ", result);
    


