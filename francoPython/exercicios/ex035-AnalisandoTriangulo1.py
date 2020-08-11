reta1 = float(input('Informe um valor de segmento de reta: '))
reta2 = float(input('Informe outro valor de segmento de reta: '))
reta3 = float(input('Informe mais outro valor de segmento de reta: '))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):

    print(f'Os segmentos de reta {reta1}, {reta2} e {reta3} podem formar um triâgulo!')

else:
    print(f'Os segmentos de reta informados não formam um triâgulo!')
