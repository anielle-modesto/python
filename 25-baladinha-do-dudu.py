print ("BALADA DO DUDU")
idade = int(input("informe sua idade:"))

if idade >= 18:
  print("entrada permitida!")
elif idade >= 16 and idade <18:
  print ("entrada permitida! somente com a autorização dos pais")
  autorizacao = input("você tem autorização dos seus pais (s/n?")
  if autorizacao.lower() == "s" or autorizacao.lower() == "sim":
    print ("entrada permitida! devido a autorização de sues pais")
  else:
    print ("entrada negada! não possui autorização dos pais")
else:
  print ("entrada negada! não possui idade suficiente")
