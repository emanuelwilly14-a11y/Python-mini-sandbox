# 18 - Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem 1,10m e cresce 3 centímetros por ano. Faça um algoritmo que calcule e imprima na tela em quantos anos serão necessários para que Sara seja maior que Francisco.

#1,50m = 150cm
#1,10m = 110cm

Francisco = 150
Sara = 110
ano = 0

while Sara <= Francisco:
    Francisco +=2
    Sara +=3
    ano +=1
f = Francisco / 100
s = Sara / 100
print(f'Em {ano} anos Sara tera {Sara}cm ou {s}m e o Francisco terá {Francisco}cm ou {f}m, teno a Sara maior que Francisco')
