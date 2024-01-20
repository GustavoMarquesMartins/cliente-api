import re
from validate_docbr import CPF


def cpf_valido(numero_do_cpf):
  """Verifica se o cpf possui 11 dígitos"""
  cpf = CPF()
  return cpf.validate(numero_do_cpf)


def nome_valido(nome_do_usuario):
  """Verifica se o nome não possui números"""
  return nome_do_usuario.isalpha()


def rg_valido(numero_do_rg):
  """Verifica se o rg possui 9 dígitos"""
  return len(numero_do_rg) == 9


def celular_valido(numero_do_celular):
  """Verifica se o celular é valido ex:(11 91234-1234)"""
  modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
  resposta = re.findall(modelo, numero_do_celular)
  return resposta