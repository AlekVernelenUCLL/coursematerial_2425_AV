def close_enough(x, y):
    return -0.1<=x-y<=0.1 or -0.1<=y-x<=0.1

a=close_enough(0, 0)

b=close_enough(0, 0.05)

c=close_enough(0, 0.1)

d=close_enough(0, -0.1)

e=close_enough(0, 0.2)

f=close_enough(18.5, 18.6)

print(a,b,c,d,e,f)