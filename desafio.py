CONSTANTE_BONUS = 1000

#1
nome_usuario = input("Digite o seu nome: ")

#2
salario = input("Digite o seu salário: ")
salario_trat = float(salario)

#3
bonus_percentual = input("Digite o percentual do seu bônus: ")
bonus = float(bonus_percentual)

#4
valor_bonus = CONSTANTE_BONUS + (salario_trat * bonus)

#5
print(f"O usuário {nome_usuario} recebeu o bonus de {valor_bonus}")

