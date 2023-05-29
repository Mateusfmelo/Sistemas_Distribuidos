import rpyc

conn = rpyc.connect("localhost", 18861) # Substitua o LocalHost pelo endereço IPV4 da rede Wi-Fi e execute

a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))

result = conn.root.sum_and_divide(a, b, c)
# Imprime o resultado da soma de a e b dividido por c
print(f"O resultado da soma de {a} e {b}, dividido por {c}, é: {result}")

conn.close()
