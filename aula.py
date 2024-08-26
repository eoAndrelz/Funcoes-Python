def saudacoes ():
    print ("Olá Mundo!")
    
saudacoes()

#Funnção com Argumentos

def saudacoes_personalizada(nome):
    print ("Olá,", nome + "!")
    
saudacoes_personalizada("Maria")

#Função com Retornos

def soma (a,b):
    resultado = a+b
    return resultado

total = soma(3,5)
print (total)

#Exemplo pratico de Funções com Retorno

def somar (x,y):
    return x+y

def subtrair (x,y):
    return x-y

def multiplicador (x,y):
    return x * y

def dividir (x, y):
    if y == 0: 
        return "Erro: Divisão por zero!"

    else: 
        return x/y 


num1 = float(input("Digite o primeiro Numero: "))
num2 = float(input("Digite o segundo Numero: "))

print("Escolha a operação: ")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

escolha = input("Digite sua escolha (1/2/3/4):")

if escolha =='1':
    print(num1,"+", num2, "=",somar(num1, num2))
elif escolha =='2':
    print(num1,"-", num2, "=",subtrair(num1, num2))
elif escolha =='3':
    print(num1,"*", num2, "=",multiplicador(num1, num2))
elif escolha =='4':
    print(num1,"/", num2, "=",dividir(num1, num2))
    
else: print("Escolha invalida")