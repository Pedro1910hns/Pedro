# Faça um programa que peça dois números inteiros Imprima a soma desses dois números na tela.

print("Escolha um número")
valor1 = int(input("número 1 = "))
valor2 = int(input("Número2 = "))
print(valor1 + valor2)
print()

# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

print("Medida (em M)")
medidam = float(input("Medida (em M) = "))
print(f"sua medida em MM é:{medidam / 1000}")

# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos

dias = int(input("dias : "))
horas = int(input("horas : "))
min = int(input("min : "))
seg = int(input("seg : "))
total_em_seg = (dias * 86400) + (horas * 3600) + (min * 60) + seg
print (total_em_seg)

# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.