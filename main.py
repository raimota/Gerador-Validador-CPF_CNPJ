from random import randint


def gerar_cpf():
  cpf = ''.join([str(randint(0, 9)) for _ in range(9)])
  while len(cpf) != 11:
    digito = sum([
        int(cpf[index]) * multiplica
        for index, multiplica in enumerate(reversed(range(2,
                                                          len(cpf) + 2)))
    ])
    cpf += str(11 - (digito % 11)) if (11 - (digito % 11)) <= 9 else '0'
  return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


def valida_cpf(cpf):
  cpf = cpf.replace('.', '').replace('-', '').strip()
  cpf_verifica = cpf
  cpf = cpf[0:9]
  while len(cpf) != 11:
    digito = sum([
        int(cpf[index]) * multiplica
        for index, multiplica in enumerate(reversed(range(2,
                                                          len(cpf) + 2)))
    ])
    cpf += str(11 - (digito % 11)) if (11 - (digito % 11)) <= 9 else '0'
  return True if cpf == cpf_verifica and cpf != (str(cpf[0]) *
                                                 len(cpf)) else False


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
  return True if cnpj == cnpj_verifica and cnpj != (str(cnpj[0]) *
                                                    len(cnpj)) else False


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


while True:
  try:
    escolha = int(
        input(
            "Escolha uma opção:\n1 - Gerar CPF\n2 - Validar CPF\n3 - Gerar CNPJ\n4 - Validar CNPJ\n5 - Sair\n\n"
        ))

    if escolha == 1:
      print(f"\nCPF GERADO: {gerar_cpf()}\n")
      
    elif escolha == 2:
      cpf = input("Digite o CPF: ")
      print(f"\nCPF Válido? {valida_cpf(cpf)}\n")
      
    elif escolha == 3:
      print(f"\nCNPJ GERADO: {gerar_cnpj()}\n")
      
    elif escolha == 4:
      cnpj = input("Digite o CNPJ: ")
      print(f"\nCNPJ Válido? {valida_cnpj(cnpj)}\n")
      
    elif escolha == 5:
      break
      
    else:
      print("\nOpção inválida\n")

  except:
    print("\nOpção inválida\n")
