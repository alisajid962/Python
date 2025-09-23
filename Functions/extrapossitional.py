def sum(a,b,c,*args):
    print(a)
    print(b)
    print(c)
    print(args)
    sum =0
    print(type(args))
    print(id(args))
    for i in args:
        sum+=i
    print("sum ",sum)
sum(2,23,4,5,6,67,7,8,)

def fun(a,b,*args,**kargs):
    print("a: ",a)
    print("b: ",b)
    print("args",args)
    print("kargs: ",kargs)
fun(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,Name="Ali",Age=20)