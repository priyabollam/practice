def myfunc(a,b):
    add=a+b
    sub=a-b
    print(add,sub)
    try:
        div=a/b
        print(div)
    except:
          print("can not divide with zero")
myfunc(a=3,b=6)