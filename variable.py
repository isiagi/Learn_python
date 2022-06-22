# variables in python

#str
x = "hello"

#num
y = 100

#dic
z = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#list
l = [1, 2, 3, 4]

#tuple
k = (1, 2, 3, 4)

#multiname

var1, var2, var3 = 1, 2, 3
print(var1)
print(var2)
print(var3)

print(k)

# one value for multi variables

r = t = y = "hello world"
print(r)
print(t)
print(y)


# destructuring in python

cars = ['bendz', 'toyota', 'ford']

first_car, second_car, third_car = cars

print(first_car)
print(second_car)
print(third_car)

# Global variable

global_var = "am gobal"

def myFun() :
    global_var = "am local"

    print(f" this is {global_var}")

print(global_var)

myFun()

#global key word variable

X = 'global'

def my_text():
    global X
    X = "local"

my_text()
print(X)
