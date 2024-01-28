from random import randint


def valida_cnpj(cnpj):
    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '').strip()
    cnpj_verifica = cnpj
    cnpj = cnpj[0:12]
    while len(cnpj) != 14:
        digito = 0
        multiplica = 5 if len(cnpj) < 13 else 6
        for n in cnpj:
            digito += (int(n) * multiplica)
            multiplica -= 1
            multiplica = 9 if multiplica == 1 else multiplica
        dv = 11 - (digito % 11)
        cnpj += '0' if dv > 9 else str(dv)
    return True if cnpj == cnpj_verifica and cnpj != (str(cnpj[0]) * len(cnpj)) else False


def gerar_cnpj():
    cnpj = ''.join([str(randint(0, 9)) for _ in range(12)])
    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '').strip()

    while len(cnpj) != 14:
        digito = 0
        multiplica = 5 if len(cnpj) < 13 else 6
        for n in cnpj:
            digito += (int(n) * multiplica)
            multiplica -= 1
            multiplica = 9 if multiplica == 1 else multiplica
        dv = 11 - (digito % 11)
        cnpj += '0' if dv > 9 else str(dv)
    return f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
