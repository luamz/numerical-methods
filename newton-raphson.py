# Example
# ⁵√175=x -> x⁵ = 175-> x⁵-175 = 0 e portanto, f(x)= x⁵-175

def f(x):
  return (x**5)-175

def derivative(x):
  return 5 * (x**4)

def newton_raphson(xo):
  return xo - ((f(xo))/(derivative(xo)))

xo = 55 #Initial Value
error = 0.00000001
max_iterations = 20

for i in range (max_iterations):
  xn = newton_raphson(xo)
  print("Iteration " + str(i+1) + ": " + str(xn))
  if (abs(xn - xo) < error):
    print("Max precision reached!")
    break
  xo = xn
