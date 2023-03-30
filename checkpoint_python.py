# Solicita dois números inteiros entre 0 e 99.
num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))

# Criando um loop com a função while para verificar se os números inseridos possuem o número 7 em qualquer posição. Se possuir será transformado para o número 0.
num1_novo = 0
num2_novo = 0

pos = 1
while num1 > 0:
    digito = num1 % 10
    if digito == 7:
        digito = 0
    num1_novo += digito * pos
    pos *= 10
    num1 //= 10

pos = 1
while num2 > 0:
    digito = num2 % 10
    if digito == 7:
        digito = 0
    num2_novo += digito * pos
    pos *= 10
    num2 //= 10

resultado = num1_novo + num2_novo

# Utilizando a mesma função while para verificar se o número 7 está presente no resultado final. Se estiver será transformado para o número 0.
resultado_novo = 0

pos = 1
while resultado > 0:
    digito = resultado % 10
    if digito == 7:
        digito = 0
    resultado_novo += digito * pos
    pos *= 10
    resultado //= 10

# Criando a restrição para que seja válido apenas número inteiros entre 0 e 99.
if 0 <= num1_novo <= 99 and 0 <= num2_novo <= 99:
    print(f'A soma entre os dois números solicitados é igual a {resultado_novo}.') # Fazendo o print da soma entre os números, onde resultado_novo é o resultado final depois da verificação feita na função while acima.
else:
    print('ERRO: apenas números inteiros entre 0 e 99 são permitidos.') # Se o usuário inserir um número que não segue a restrição feita na linha 42, fazer o print de uma mensagem de erro.