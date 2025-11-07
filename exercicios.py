# ativar env = source .venv/Scripts/activate
# desativar env = deactivate
# flag executa exercicio
executa = True

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
executa = False # pula
if executa:
    print('Some de 2 inteiros')
    num1_str = input('Digite um valor: ')
    num2_str = input('Digite outro valor: ')
    num1 = int(num1_str)
    num2 = int(num2_str)
    soma = num1 + num2
    print(f'A soma de {num1} e {num2} é {soma}')
else:
    print('Pulei 1.')
    executa = True

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
executa = False # pula
if executa:
    print('Restp de 5')
    num1_str = input('Digite um valor: ')
    num1 = int(num1_str)
    resto_5 = num1 % 5
    print(f'O resto da divisão de {num1} e 5 é {resto_5}')
else:
    print('Pulei 2.')
    executa = True
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
executa = False # pula
if executa:
    print('Multiplicação de 2 numeros')
    num1_str = input('Digite um valor: ')
    num2_str = input('Digite um valor: ')
    num1 = int(num1_str)
    num2 = int(num2_str)
    multiplicacao = num1 * num2
    print(f'A multiplicação de {num1} e {num2} é {multiplicacao}')
else:
    print('Pulei 3.')
    executa = True

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

executa = False # pula
if executa:
    print('Divisao inteira')
    num1_str = input('Digite um valor: ')
    num2_str = input('Digite um valor: ')
    num1 = int(num1_str)
    num2 = int(num2_str)
    div_inteira = num1 // num2
    print(f'A divisão inteira de {num1} por {num2} é {div_inteira}')
else:
    print('Pulei 4.')
    executa = True
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
executa = False # pula
if executa:
    print('Quadrado de numero')
    num1_str = input('Digite um valor: ')
    num1 = int(num1_str)
    
    potencia = num1 ** 2
    print(f'O quadrado de {num1} é {potencia}')
else:
    print('Pulei 5.')
    executa = True

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
executa = False # pula
if executa:
    print('Adicao de Float')
    num1_str = input('Digite um valor: ')
    num2_str = input('Digite um valor: ')
    num1 = float(num1_str)
    num2 = float(num2_str)
    soma = num1 + num2
    print(f'A adição de {num1} por {num2} é {soma:.1f}')
else:
    print('Pulei 6.')
    executa = True
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# executa = False # pula
if executa:
    print('Media')
    num1_str = input('Digite um valor: ')
    num2_str = input('Digite um valor: ')
    num1 = float(num1_str)
    num2 = float(num2_str)
    media = (num1 + num2) / 2
    print(f'A media de {num1} por {num2} é {media:.1f}')
else:
    print('Pulei 7.')
    executa = True
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação