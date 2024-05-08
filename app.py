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

    elif opcao == 2:
       for c in range (0,len(pessoas)):
          p = pessoas[c]
          print(f"\n cod: {c}\n nome: {p.nome}\n sobrenome: {p.sobrenome}\n email: {p.email}\n telefone: {p.telefone}\n")
          
    elif opcao == 3:
        escolhida = int(input('informe aqui a pessoa a ser editada: '))
        p= pessoas[escolhida]
        p.nome = input('Nome: ')
        p.sobrenome = input('Sobrenome: ')
        p.email = input('E-mail: ')
        p.telefone = input('Telefone: ')
        print(pessoas[escolhida].nome)

       

    
    print(menu)

    