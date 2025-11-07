# tratando erros
import datetime

try:
    ano_str = input('Informe seu ano nascimento: ')
    
    ano_int = int(ano_str)

    # ano_int = float(ano_str) # forçar erro instancia

    # inspecionar instancia
    if isinstance(ano_int, int):
        idade = datetime.datetime.now().year - ano_int
    else:
        idade = 0

    print(f'Sua idade é {idade}')
except (ZeroDivisionError, TypeError, ValueError) as e: # erros provaveis
    print(e)
except KeyboardInterrupt as e:
    print('Usuário abortou processo')
except: # erros desconhecidos
    print('erro desconhecido')
else:
    print('programa sem erro')
finally:
    print('fim do programa')