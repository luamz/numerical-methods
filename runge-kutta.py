from math import log

# Runge-Kutta 4th order

def f(y, t):
    return ( log((y * t)) ) + ( (y ** 2) * t )

def k1(h, wi, ti):
    return h * (f(wi,ti))

def k2(h, wi, ti, k1):
    return h * (f ( (wi + (k1/2) ), (ti + (h/2)) ) )

def k3(h, wi, ti, k2):
    return h * (f ( (wi + (k2/2) ), (ti + (h/2)) ) )

def k4(h, wi, ti, k3):
    return h * (f ( (wi + k3 ), (ti + h) ) )

def runge_kutta(wi, h, ti):
    k_1 = k1(h, wi, ti)
    k_2 = k2(h, wi, ti, k_1)
    k_3 = k3(h, wi, ti, k_2)
    k_4 = k4(h, wi, ti, k_3)
    return wi + (1/6) * (k_1+ (2*k_2) + (2*k_3) + k_4)


# Intervals
a = 1.0
b = 5.0

# Number of steps
n = 40

# Steps
h = (b-a) / n
t = [round((a+(step*h)), len(str(n))) for step in range(n)]

w0 = 0.5
w1 = runge_kutta(w0, h, t[0])

print("w0 = {}, w1 = {}".format(w0, round(w1,12)))

