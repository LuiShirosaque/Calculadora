def add(x,y):
  return x+y

def sub(x,y):
  return x-y

def mult(x,y):
  return x*y

def div(x,y):
  return x/y

print("selecione uma operação")
print("1. adição")
print("2. subtração")
print("3. multiplicação")
print("4. divisão")

escolha = input("escolha uma operação(1/2/3/4)")

if escolha in ('1','2','3','4'):
  n1 = float(input("digite um número: "))
  n2 = float(input("digite outronúmero: "))

if escolha == '1':
  print(n1,"+",n2,"=",add(n1,n2))

if escolha == '2':
  print(n1,"-",n2,"=",sub(n1,n2))

if escolha == '3':
  print(n1,"*",n2,"=",mult(n1,n2))

if escolha == '4':
  print(n1,"/",n2,"=",div(n1,n2))

