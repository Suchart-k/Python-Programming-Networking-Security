# Assert for any conditions
x = 0
assert x == 0, "X must be 0 only"

f = lambda x: x*x
assert f(2) == 4
assert f(3) == 9

y = 5
value = 0
if y < 5:
    value = -1
elif y > 5:
    value = 1
else:
    value = 0
assert value == 0


