saldo = 1000
saque = 200
limite = 100

print (saldo >= saque and saque <= limite)

saldo = 1000
saque = 200
limite = 100

print (saldo >= saque or saque <= limite)

contatos_emergencia = [] # símbolo de lista mas nesse caso a lista está vazia, o que seria considerado falso em python, ao colocar o not antes significa que se quer indicar o contrário.

not 1000 > 1500 # vai dar verdadeiro/true pq 1000 não é maior que 1500, mas con o not na frente ele significa o inverso
not contatos_emergencia # vai dar true pq lista vazia = falso e o not puxa para o contrário
not "saque 1500;" # vai dar falso
not "" # str vazia também é falso


#parenteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print (exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print (exp_3)