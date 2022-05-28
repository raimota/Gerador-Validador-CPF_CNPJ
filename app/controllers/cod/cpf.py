from random import randint


def gerar_cpf():
    cpf = ''.join([str(randint(0, 9)) for _ in range(9)])
    while len(cpf) != 11:
        digito = sum([int(cpf[index]) * multiplica for index,
                     multiplica in enumerate(reversed(range(2, len(cpf)+2)))])
        cpf += str(11 - (digito % 11)) if (11 - (digito % 11)) <= 9 else '0'
    return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


def valida_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '').strip()
    cpf_verifica = cpf
    cpf = cpf[0:9]
    while len(cpf) != 11:
        digito = sum([int(cpf[index]) * multiplica for index,
                     multiplica in enumerate(reversed(range(2, len(cpf)+2)))])
        cpf += str(11 - (digito % 11)) if (11 - (digito % 11)) <= 9 else '0'
    return True if cpf == cpf_verifica and cpf != (str(cpf[0]) * len(cpf)) else False
