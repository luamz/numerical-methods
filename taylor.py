from traceback import print_tb


def f(t,w):
    return -w + t + 2

def f_l(t,w):
    return w - t -1

def f_ll(t,w):
    return -w + t + 1

def f_lll(t,w):
    return w - t - 1

def taylor(t,w,h):
    return f(t,w) + ((h/2)*(f_l(t,w))) + (((h**2)/6)*(f_ll(t,w))) + (((h**3)/24)*(f_lll(t,w)))

h=0.1
t=0
w0 = 2

taylor1 = taylor(t,w0,h)
w1 = w0 + (h*taylor1)
print("w0={}, w1 = {}, T1(4) = {}".format(w0, w1, taylor1))