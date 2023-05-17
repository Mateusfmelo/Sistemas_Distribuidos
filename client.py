import rpyc

conn = rpyc.connect("localhost", 18861) # Substitua o LocalHost pelo endereço IPV4 da rede Wi-Fi

a = 10
b = 5
c = 3

result = conn.root.sum_and_divide(a, b, c)
# Imprime o resultado da soma de a e b dividido por c
print(f"O resultado da soma de {a} e {b}, dividido por {c}, é: {result}")

conn.close()
