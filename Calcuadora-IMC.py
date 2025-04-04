
print ("====CALCULADORA IMC ====")


def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso adequado"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade I"
    elif 35 <= imc < 39.9:
        return "Obesidade II"
    else:
        return "Obesidade III"
print()
# Entrada de dados
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
print()

# Cálculo do IMC
imc = calcular_imc(peso, altura)
categoria = interpretar_imc(imc)

# Resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Categoria: {categoria}")
