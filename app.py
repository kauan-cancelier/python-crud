class Contato:
    def __init__(self):
        self.id = 0
        self.nome_completo = ''
        self.email = ''
        self.numero = ''

    def set_nome_completo(self, nome_completo: str):
        while not nome_completo.strip():
            print("O nome completo não pode estar vazio.")
            nome_completo = input('Digite o nome completo: ')
        self.nome_completo = nome_completo

    def set_email(self, email: str):
        while not email.strip():
            print("O e-mail não pode estar vazio.")
            email = input('Digite o e-mail: ')
        self.email = email

    def set_numero(self, numero: str):
        while not numero.strip():
            print("O número de telefone não pode estar vazio.")
            numero = input('Digite o número de telefone: ')
        self.numero = numero

    def exibir_contato(self):
        print(f'\nCódigo: {self.id}')
        print(f'Nome completo: {self.nome_completo}')
        print(f'E-mail: {self.email}')
        print(f'Telefone: {self.numero}\n')

contatos = []

def formulario(contato: Contato):
    print('------------------------------------')
    print('\nCadastro de contatos: \n')
    contato.set_nome_completo(input('Digite o nome completo: '))
    contato.set_email(input('Digite o e-mail: '))
    contato.set_numero(input('Digite o número de telefone: '))
    return contato

def inserir():
    p = Contato()
    p = formulario(p)
    p.id = len(contatos) + 1
    contatos.append(p)
    print('\nContato cadastrado com sucesso!')

def mostrar_contatos():
    if len(contatos) == 0:
        print("\nNenhum contato cadastrado.\n")
    else:
        print('\nLista de contatos\n')
        for p in contatos:
            p.exibir_contato()

def editar(contato: Contato):
    formulario(contato)
    print('Contato editado com sucesso!')

def menu():
    print('\nMenu')
    print('1 - Novo contato')
    print('2 - Ver contatos')
    print('3 - Editar contato')
    print('4 - Encerrar\n')
    try:
        return int(input('Escolha uma opção do menu: '))
    except:
        print('\nDigite uma opção válida.')
        return 0

opcao_escolhida = 0

while opcao_escolhida != 4:
    opcao_escolhida = menu()
    if opcao_escolhida == 1:
        inserir()
    elif opcao_escolhida == 2:
        mostrar_contatos()
    elif opcao_escolhida == 3:
        if len(contatos) == 0:
            print("Não há contatos para editar.")
        else:
            mostrar_contatos()
            try:
                quem_editar = int(input('Digite o código do contato que deseja editar: '))
                if quem_editar <= 0 or quem_editar > len(contatos):
                    print("Código de contato inválido.")
                else:
                    contato_editar = contatos[quem_editar - 1]
                    editar(contato_editar)
            except ValueError:
                print("Por favor, digite um número válido.")
    elif opcao_escolhida == 4:
        print('Saindo...')
    else:
        print('Opção inválida.')
