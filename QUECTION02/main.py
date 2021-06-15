
from StackLinked import StackLinked

stack = StackLinked()



print("------------------------------------")
print("-\t\t\"EMPTY STACK LIST \"        - \n\n")



stack.peek()
print("=====================================\n")



print("------------------------------------")
print("-\t\t\"PUSH ELEMENT \"            -")
print("------------------------------------\n")



stack.push("rashmi")
stack.push("saman")
stack.push("kamal")
stack.push("sunimal")
stack.push("samana dissanayaka")




print("\n\n=====================================")
print("\tTop element is >>> ", stack.peek())
print("=====================================\n")


print("\n=====================================")
print("\t stack size is >>> ", stack.size())
print("=====================================\n")



print("\n=====================================")
stack.pop()
print("=====================================")

print("\n=====================================")
print("\t stack size is >> ", stack.size())
print("=====================================\n")


print("\n=====================================")
print("\tTop element is >> ", stack.peek())
print("=====================================\n")


print("\n=====================================")
stack.pop()
stack.pop()
stack.pop()
print("=====================================")



print("\n=====================================")
print("\t stack size is >> ", stack.size())
print("=====================================\n")



print("\n=====================================")
stack.pop()
print("=====================================")


print("\n=====================================")
print("\t stack size is >> ", stack.size())
print("=====================================\n")



print("\n=====================================")
stack.pop()
print("=====================================\n\n")


print("============isEMPTY RESULT=================")
print(stack.isEmpty())