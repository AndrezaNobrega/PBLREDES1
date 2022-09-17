totalLitros = 654654
metrosC = totalLitros/1000

if totalLitros <= 6000:
    valorReais = 28,82
if metrosC > 7 and 10:
    valorReais = (metrosC - 6)*1.17 + 28.82
if metrosC > 11 and 15:
    valorReais = (metrosC - 11)*7.4 + 28.82
if metrosC > 16 and 20:
    valorReais = (metrosC - 16)*8 + 28.82
if metrosC > 21 and 25:
    valorReais = (metrosC - 21)*10.51 + 28.82
if metrosC > 26 and 30:
    valorReais = (metrosC - 26)*11.71 + 28.82
if metrosC > 31 and 40:
    valorReais = (metrosC - 31)*12.90 + 28.82
if metrosC > 41 and 50:
    valorReais = (metrosC - 41)*14.79 + 28.82
if metrosC > 50:
    valorReais = (metrosC - 50)*17.78 + 28.82
valorReais = "{:.2f}".format(valorReais)
print('o valor da sua conta é:', valorReais)