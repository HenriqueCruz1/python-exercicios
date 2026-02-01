
print('-'*15,' CAIXA ELETRONICO ','-'*15)

cedula_1 = 0
cedula_10 = 0
cedula_20 = 0
cedula_50 = 0
cedula = 0
cedulas = 0

valor_sacado = int(input('Qual será o valor a ser sacado? '))
total = valor_sacado
while True:

    if total == 0:
        break

    if total >= 50:
        cedula = 50
        total -= cedula
        cedula_50 += 1
        cedulas +=1

    elif total >= 20:
        cedula = 20
        total -= cedula
        cedula_20 += 1
        cedulas += 1

    elif total >= 10:
        cedula = 10
        total -= cedula
        cedula_10 += 1
        cedulas += 1

    else:
        cedula = 1
        total -= cedula
        cedula_1 += 1
        cedulas += 1

print(f'O valor sacado foi {valor_sacado} R$ ')
print(f'Composto por {cedula_50} cedulas de 50 R$')
print(f'{cedula_20} cedulas de 20 R$')
print((f'{cedula_10} cedulas de 10 R$'))
print(f'{cedula_1} cedulas de 1 R$')
print('FIM')








