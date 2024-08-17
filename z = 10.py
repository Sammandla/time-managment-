z = 10

def func1():

  global z

  z = 3

def func2(x,y):

  global z

  return x+y+z

total = func2(4,5)

func1()

print(total)