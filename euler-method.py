import math
# Intervals
a = 0.0
b = 2.0

# Number of steps
n = 10

# Steps
h = (b-a) / n
t = [round((step*h),2) for step in range(n)]

# y' = f(t,y)
def f(t,y):
    return y - (t**2) +1

# Initial value
wo = 0.5

# Iteration
def w(wi,ti,h):
    return wi + h * (f(ti,wi))

#Method
print("----- Euler Method-----")
print('a = {}, b = {}, n = {}, h = {}\n'.format(a, b, n, h))
print('wo = {} (initial value)'.format(wo))

wi = wo
for ti in t:
    i = int((ti*n)/b)+1
    wi = w(wi,ti,h)
    print('w{} = {}, t{} = {}'.format(i, round(wi,12), i-1, ti))