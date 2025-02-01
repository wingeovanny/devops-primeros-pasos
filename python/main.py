def sumar():
    a = int(input("Indique primer valor: "))
    b = int(input("Indique segundo valor: "))
    return a + b

def cat(file):
    f = open(file, 'r')
    print(f.read())

cat("main.py")