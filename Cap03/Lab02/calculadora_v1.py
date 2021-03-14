# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")


print("\n Selecione a operação desejada \n \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação\n 4 - Divisão ")

selecao = int(input("\nDigite sua opção (1/2/3/4:)"))

n1 = int(input("\nDigite o primeiro número: "))

n2 = int(input("\nDigite o segundo número: "))


# SOMA
if selecao == 1:
    soma =  n1+n2
    print("\nResultado: ", soma)

# SUBTRAÇÃO
elif selecao == 2:
    subtracao =  n1-n2
    print("\nResultado: ", subtracao)

# MULTIPLICAÇÃO
elif selecao == 3:
    multiplicacao =  n1*n2
    print("\nResultado: ", multiplicacao)

# DIVISAO
elif selecao == 4:
    divisao =  n1//n2
    print("\nResultado: ", divisao)

else:
    print("\nSeleção inválida!")