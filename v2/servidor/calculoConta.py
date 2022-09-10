totalLitros = 16050


if totalLitros <= 6000:
    valorReais = 28,82
elif totalLitros > 7000 and 10000:
    valorReais = (((6000-totalLitros)/1000)*1,17)+28,82
elif totalLitros > 11000 and 15000:
    valorReais = (((11000-totalLitros)/1000)*7,4)+28,82
elif totalLitros > 16000 and 20000:
    valorReais = (((16000-totalLitros)/1000)*8)+28,82
elif totalLitros > 21000 and 25000:
    valorReais = (((21000-totalLitros)/1000)*10,51)+28,82
elif totalLitros > 26000 and 30000:
    valorReais = (((26000-totalLitros)/1000)*11,71)+28,82
elif totalLitros > 31000 and 40000:
    valorReais = (((31000-totalLitros)/1000)*12,90)+28,82
elif totalLitros > 41000 and 50000:
    valorReais = (((41000-totalLitros)/1000)*14,79)+28,82
else:
    valorReais = (((50000-totalLitros)/1000)*17,78)+28,82

print('o valor da sua conta é:', valorReais)