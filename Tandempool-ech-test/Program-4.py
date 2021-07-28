lis = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

n = int(input("Enter the elements in list :"));

inp_list = [];

dist = {}

print("\n Enter the elements : \n")
for x in range(0,n):
    inp = int(input("\n"));
    inp_list.append(inp);



for x in lis:
    count = 0;
    for y in inp_list:
        if y % x == 0:
            count = count + 1;

    dist[x] = count;



print(dist)
