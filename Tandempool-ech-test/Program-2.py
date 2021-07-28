a = int(input("Enter the number: \n"));

if a == 1:
    print("output: ", 1)

else:
    print(1,end = " ,");
    a = a * 2;
    for x in range(2,a):
        if x % 2 != 0:
            print(x , end = " ,");
