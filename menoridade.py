# CONFERIR SE USUÁRIO É MENOR DE IDADE OU NÃO
nome = input ("Digite seu nome: ")
idade = int(input('Digite sua idade: '))
maior_de_idade = idade >= 18

print("Nome:", nome)
print('Idade:', idade)
print('É maior?', maior_de_idade)