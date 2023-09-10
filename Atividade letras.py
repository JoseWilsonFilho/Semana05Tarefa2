def letras(x):
    if x.isalpha():
        return True
    else:
        return False
x=input()
x=x.lower()
r=letras(x)
print(r)
