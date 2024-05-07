# initialization
class Pessoa:
  def __init__(self, nome, sobrenome, email, telefone):
    self.nome = nome
    self.sobrenome = sobrenome
    self.email = email
    self.telefone = telefone




pessoas = []




menu =  " 1 - Adicionar\n 2 - Visualizar\n 3 - Editar\n 4 - Sair"

print('Menu de Opções')
print(menu)

opcao = 0

while opcao != 4:
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nome = input('Nome: ')
        sobrenome = input('Sobrenome: ')
        email = input('E-mail: ')
        telefone = input('Telefone: ')
        p1 = Pessoa(nome, sobrenome, email, telefone)
        pessoas.append(p1)
        print('Pessoa adicionada com SUCESSO')

    print(menu)