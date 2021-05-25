# Desafio - If Else - Ponto do Steak
'''
Cenário: Tenho um termometro e coloco o termometro na carne,
 e a partir da temperatura coletada é possível identificar se 
 a carne esta ao ponto, mal passada, cru, bem passada etc.

Criar um programa que dependendo da temperatura (em celsius)
 do steak (carne) ele retorna o ponto de cozimento em PT-BR, 
 o usuário deverá fornecer a temperatura.

Temperaturas - cozimento 

120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (Bem passada)


valor = int(input('Qual é a temperatura da carne? '))

print(valor)

while valor >= -1:
    valor = (valor >= 46) + valor
    print(f' O valor da carne é de:{valor}')
    break
'''

'''
temperatura = 48


    resultado = print('A carne esta selada!')
elif temperatura < 48:
    resultado = print('Precisa assar mais um pouco!')
else:
    print('Favor digitar a temperatura da carne:')


'''
'''
temperatura_Cel = int(input('Digite a temperatura coletada da carne:'))

if temperatura_Cel  < 48:
    print('Precisa assar mais um pouco!')

elif temperatura_Cel in range(48, 53):
    print('Sua carne esta selada')    
elif temperatura_Cel in range(53, 54):
    print('Sua carne esta ao ponto para o mal passado')
elif temperatura_Cel in range(59, 60):
    print('Sua carne esta ao ponto')
elif temperatura_Cel in range(64, 70):
    print('Sua carne esta ao ponto para o bem')        
elif temperatura_Cel >= 71:
    print('Sua carne esta bem passada')

print(temperatura_Cel)
'''
'''    
elif temperatura >= 48:
    resultado = print('Sua carne esta ao ponto para o mal passado')
  

if valor < 54:
    resultado = print('Sua carne esta selada!')
elif valor >= 60:
    resultado = print('Sua carne esta ao ponto!')

if valor < 60:
    resultado = print('Precisa assar mais um pouco!')
elif valor >= 65:
    resultado = print('Sua carne esta ao ponto para o bem passado.')

if valor < 65:
    resultado = print('Precisa assar mais um pouco!')
elif valor >= 71:
    resultado = print('Sua carne esta bem passada!')

'''    


'''
120ºF ou 48ºC - Rare (Selada) ok 
130ºF ou 54ºC - Medium rare (Ao ponto para o mal) ok
140ºF ou 60ºC - Medium (Ao ponto) ok
150ºF ou 65ºC - Medium well (Ao ponto para o bem) ok 
160ºF ou 71ºC - Well done (Bem passada) ok



while valor >= 1:
    valor = (valor * 1) + valor
    print(f' Sua carne esta selada {valor}')
    break

def temperatura():
    temp1 = 0
    temp2 = 47
    resultado = temp1 >= temp2
    print(resultado)

temperatura('VOLTA PRO FOGO')



    
'''

# RESULTADO DO PROFESSOR:
'''
tem_cel = int(input('Qual é a temperatura da carne? '))

if tem_cel < 48:
    print('Cozinhar por mais alguns minutos')

    
elif tem_cel in range(48, 53):
    print('Selada')    
elif tem_cel in range(53, 54):
    print('Ao ponto para o mal')
elif tem_cel in range(59, 60):
    print('Ao ponto')
elif tem_cel in range(64, 70):
    print('Ao ponto para o bem')        
elif tem_cel >= 71:
    print('Bem passada')

print(tem_cel)

'''









































