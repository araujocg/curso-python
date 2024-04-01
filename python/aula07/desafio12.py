preco = float(input('Qual o preço do Produto? R$:'))
desconto = (preco*10/100)
print(f"O Produto que custava {preco}R$, na promoção com desconto de 5% vai custar {preco - desconto:.2f}")