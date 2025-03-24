# calculadora de IMC
nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura (em metros): '))
peso = float(input('Digite seu peso (em kg): '))
imc = peso / (altura ** 2)

print(f'Olá, {nome}. Vamos calcular seu IMC?')
print(f'Seu IMC é: {imc}')

if imc < 18.4:
    print('Categoria: Subpeso')
elif 18.5 <= imc < 24.9:
    print('Categoria: Normal')
elif 25 <= imc < 29.9:
    print('Categoria: Sobrepeso')
elif 30 <= imc < 34.9:
    print('Categoria: Obesidade grau 1')
elif 35 <= imc < 39.9:
    print('Categoria: Obesidade grau 2')
else:
    print('Categoria: Obesidade grau 3')