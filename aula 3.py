media_final = float(input("média final ="))

if media_final >= 6:
    print("aprovado")
else:
    print("Reproado")

#ex 1

vel = int(input("velocidade em km/h = "))
if vel > 80:
    print("Multado.")
    multa = ( vel - 80) * 5
    print(f"O valor da multa é R${multa:.2f}")

#ex 3

valor1 = float(input("insira um número = "))
valor2 = float(input("insira outro número = "))
valor3 = float(input("insira o terceiro Número = "))

maior = valor1
if valor2 >= valor1 and valor2 >= valor3:
    maior = valor2
if valor3 >= valor1 and valor3 >= valor2:
    maior = valor3
print(maior)

menor = valor1
if valor2 <= valor1 and valor2 <= valor3:
    menor = valor2
if valor3 <= valor1 and valor3 <= valor2:
    menor = valor3
print(menor)

#ex3

salario = float(input("salário"))





#ex4

distancia = int(input("Distância desejada : "))
if distancia <= 200:
    preco = (distancia * 0.50)
    print(f"Preço da passagem : R${preco} ")
else:
    preco = distancia * 0.45
    print(f"Preço da passagem : R${preco} ")

