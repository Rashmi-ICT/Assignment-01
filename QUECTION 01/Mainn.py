from Array import stack

mystack =stack(5)


print("===================================================")
mystack.isEmpty()
print("===================================================\n")


print("~~~~~~~~~~~~~~~~~~PUSH ELEMENT~~~~~~~~~~~~~~~~~~~~~~~\n")
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
print("===================================================\n")


print("~~~~~~~~~~~~~~~~~~TOP ELEMENT~~~~~~~~~~~~~~~~~~~~~~~\n")
mystack.top()
print("==================================================\n")


print("~~~~~~~~~~~~~~~~~~STACK LENGTH~~~~~~~~~~~~~~~~~~~~~~~\n")
x = mystack.size()
print("STACK LENGTH IS ", x)
print("===================================================\n")

mystack.pop()


x = mystack.size()
print("stack LENGTH IS ", x)


mystack.isFull()

mystack.pop()
mystack.pop()
mystack.pop()


mystack.top()


x = mystack.size()
print("stack LENGTH IS")




