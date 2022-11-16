# UPN : Umgekehrte Polnische Notation

upn = input("Geben Sie einen UPN ein:").split(" ")
stack = []
for i in upn:
    print(stack)
    if i.isnumeric():
        stack.append(i)
    elif i in "**/-":
        a = stack.pop()
        b = stack.pop()
        stack.append(str(eval(b+"**"+a)))
    else:
        stack.append(str(eval(stack.pop()+i+stack.pop())))
print(stack)
print(stack)
