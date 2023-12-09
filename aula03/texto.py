faturamento = 1000
custo = 700
lucro = faturamento- custo

print(f"Faturamento:{faturamento}, Custo:{custo}, lucro:{lucro}")
print("Faturamento:",faturamento,", Custo:",custo,", lucro:",lucro)
print("Faturamento: " + str(faturamento)) #Precisa do str() pq só da pra concatenar Strings

email = "Draki.araujo@gmail.com" # diferente um do outro
email = "DRAKI.ARAUJO@gmail.com" #
print(email.lower()) # draki.araujo@gmail.com
print(email.upper()) # DRAKI.ARAUJO@GMAIL.COM
print(email.find("@")) # -1 se ele n encontrar o "elemento"
print(email[12:]) # @gmail.com