def myfunc():
    a=int(input("enter a values = "))
    b=int(input("enter a values = "))
    sum=a+b
    mul=a-b
    print(sum,mul)
    try:
        div=a/b
    except:
        print("not divided with zero")
    else:
        print(div)
myfunc()