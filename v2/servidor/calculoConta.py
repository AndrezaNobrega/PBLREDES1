totalLitros = 16050
metrosC = totalLitros/1000

if totalLitros <= 6000:
    valorReais = 28,82
    if valorReais > 7 and 10:
        valorReais = (600 - metrosC)*1.17 + 28.82
        if valorReais > 11000 and 15000:
            valorReais = (1100-metrosC)*7.4 + 28.82
            if valorReais > 16000 and 20000:
                valorReais = (1600-metrosC)*8 + 28.82
                if valorReais > 21000 and 25000:
                    valorReais = (2100-metrosC)*10.51 + 28.82
                    if valorReais > 26000 and 30000:
                        valorReais = (2600-metrosC)*11.71 + 28.82
                        if valorReais > 31000 and 40000:
                            valorReais = (3100-metrosC)*12.90 + 28.82
                            if valorReais > 41000 and 50000:
                                valorReais = (4100-metrosC)*14.79 + 28.82
                                if valorReais > 5000:
                                    valorReais = (5000- metrosC)*17.78 + 28.82

print('o valor da sua conta é:', valorReais)