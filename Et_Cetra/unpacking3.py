def f(*args, **kwargs):
    print("Positional arguments:",  args)
    print("Named:", kwargs)


f(100,50,23)
f(g=100,s=50,k=23)
