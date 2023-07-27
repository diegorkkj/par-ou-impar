x = "n"

while x !="y":

    if 2 > 1:
        print("Bem vindo ao eres_coca_or_fanta. py,")
        print("O melhor algoritimo de par ou impar q ta tendo.")

    x = int(input("Informe o numero: "))

    sobra = x % 2

    if sobra == 0:
        print("É coca")

    else:  
        print("É fanta")

    x = input("Deseja sair? \n y = SIM \n n = NÃO \n")
    if x == "Y" or x == "sim":
        x = "y"
    elif x == "N" or x == "não":
        x = "n"

