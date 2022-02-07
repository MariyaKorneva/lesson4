#n=1
#x=10
#while x<=20:
    #n=n+1
    #x=x+0.1*x
    #print("{:3}".format(n), "{:6.1f}".format(x))

#print("вычислите значение функции y=x^2")
#x=1
#while x<=10:
    #y=x**2
    #print(y)
    #x+=1

#print("вычислите значение функции y=x^2")
#x=1
#while x<=10:
    #y=x**2
    #print(f"число {x}, квадрат которого {y}")
    #x+=1

#print("s=1+2+3+....+n")
#n=int(input("Введите ваше число"))
#s=0
#x=1
#while x<=n:
    #s+=x
    #x+=1
    #print(s)

#print("S=1+3+5+7+...+n")
#n=int(input("Введите n"))
#Sum=0
#i=1
#while i<=n: 
    #Sum+=i
    #i+=2
#print(Sum)

#print("k!=1*2*3*...*k")
#k=int(input("Введите k:"))
#i=1
#Mul=1
#while i<=k:
    #Mul*=1
    #i+=1
#print(Mul)

#print("k!=1*2*3*...*k")
#k=int(input("введите k:"))
#i=1
#Mul=1
#while i<=k:
   # Mul*=i
    #i+=1
#print(Mul,"$")

print("s=1/2+1/4+1/8+...")
n=int(input("введите количество слагаемых"))
s=0
i=1
a=1/2
while i<=n:
    s+=a
    i+=1
    a/=2
print(s)