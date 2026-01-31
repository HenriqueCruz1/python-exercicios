# Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar . No final , mostre:

#Qual é o total gasto na compra.
#Quantos produtos custam mais de R$ 1000.
#Qual é o nome do produto mais barato.
total_gasto = 0
produtos_mais_de_mil = 0
produto_mais_barato = 0
nome_produto_mais_barato = ''

while True:
    nome_produto = str(input('Qual o nome do produto? '))
    preco_produto = int(input('Qual o preço do produto? '))

    total_gasto += preco_produto

    if preco_produto > 1000:
        produtos_mais_de_mil += 1

    if produto_mais_barato == 0 or preco_produto < produto_mais_barato:
        produto_mais_barato = preco_produto
        nome_produto_mais_barato = nome_produto

    pergunta = str(input('Passar novo produto? [S/N]')).strip().upper()
    if pergunta != 'S':
        break
print(f'O total gasto da compra foi {total_gasto:.2f}')
print(f'A quantidade de produtos com valor maior que 1000R$ são {produtos_mais_de_mil}')
print(f'O produto mais barato é {nome_produto_mais_barato} custando R$ {produto_mais_barato:.2f}')






