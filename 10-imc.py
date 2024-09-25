print("programa para calcular de IMC")
peso = float(input("digite seu peso (em kg):"))
altura = float(input("Digite a sua altura(em metros):"))
imc = peso / (altura ** 2)

print(f"seu imc é {imc:.2f}")
print ("classificação do IMC")
if imc < 18.5:
    print("abaixo do peso normal")
elif 18.5 <= imc <25:
    print("peso normal")
elif 25 <= imc < 35:
    print("sobrepreso")
else:
    print("obesidade.")
