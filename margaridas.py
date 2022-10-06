def conversao_cm_pol ():
  valor_cm = float(input("Digite o valor em centímetros: "))
  valor_pol = valor_cm/2.54
  file = open('flor.txt', "w+")
  file.write(print("o valor", valor_cm, " em centímetros corresponde a", valor_pol,", valor em polegadas"))
  print(file.read())