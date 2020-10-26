i = 10

'''while i > 0:
    while x != 0:
        print("x=",x)
        x -= 1
    print(i)
    i-=1'
y=5
for x in range(i):
    print(x)
    for y in range(10):
        print("y=",y)'''

f = open("Execution_Times","r")
contents = f.read().split()
print(contents)
print("-"*20)
data = contents[5::]
print("data = ",data)