

print("enter name und family")
name =input()


average = 0

for i in range (1, 4):
    print("numrato",i," vard kon")
    n = float(input())
    average = average + n

average = average / 3

if average > 17 :
    print("momtaz")
elif average > 12 and average<17:
    print("adie")    
elif average < 12:
    print("mashrot")


