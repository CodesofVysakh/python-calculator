x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = input('Enter your choice ("+","-","*","/"): ')

def calc(a,b,c):
    ans = 0
    if c == "+":
        ans = a+b
    elif c == "-":
        ans = a-b
    elif c == "*":
        ans = a*b
    elif c == "/":
        ans = a/b
    print("Solution : ", ans)

calc(x,y,z)