from math import log

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
    k_1 = k1(h,wi,ti)
    k_2 = k2(h,wi,ti,k_1)
    k_3 = k3(h,wi,ti,k_2)
    k_4 = k4(h,wi,ti,k_3)
    return wi + (1/6) * (k_1+ (2*k_2) + (2*k_3) + k_4)


def adams_bashforth_4th(w0, w1, w2, w3, h, t):
    p_1 = 55 * f(w3,t[3])
    p_2 = 59 * f(w2,t[2])
    p_3 = 37 * f(w1,t[1])
    p_4 =  9 * f(w0,t[0])
    return w3 + ( (h/24) * (p_1 - p_2 + p_3 - p_4) )

def adams_moulton_3rd(w1, w2, w3, w4_0, h, t):
    p_1 =  9 * f(w4_0, t[4])
    p_2 = 19 * f(w3,t[3])
    p_3 =  5 * f(w2,t[2])
    p_4 = f(w1,t[1]) 
    return w3 + ( (h/24) * (p_1 + p_2 - p_3 + p_4) )

def q(h, error, w4_1, w4_0):
    return 1.5 * ( ( (h * error) / (abs(w4_1 - w4_0)) ) ** (1/4))


# Intervals
a = 1.0
b = 5.0

# Number of steps
n = 40

# Steps
h = (b-a) / n
t = [round((a+(step*h)),len(str(n))) for step in range(n)]

# Error
error = 10**(-2)

# Iterations
w0 = 0.5
w1 = runge_kutta(w0, h, t[0])
w2 = runge_kutta(w1, h, t[1])
w3 = runge_kutta(w2, h, t[2])
w4_0 = adams_bashforth_4th(w0, w1, w2, w3, h, t)
w4_1 = adams_moulton_3rd(w1,w2,w3,w4_0,h,t)
q_ = q(h, error, w4_1, w4_0)

print("  w0 = {}\n  w1 = {}\n  w2 = {}\n  w3 = {}\nw4_0 = {}\nw4_1 = {}"
     .format(round(w0,12), round(w1,12), round(w2,12), round(w3,12), round(w4_0,12), round(w4_1,12)))

print("   q = {}".format(round(q_,12)))
if q_ > 1.0:
    print("Accepts step")
else:
    print("Rejects step")