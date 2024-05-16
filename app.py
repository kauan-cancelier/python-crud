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
        print(f'\nCódigo: {self.id} \n  Nome completo: {self.nome_completo}\n  Telefone: {self.numero}\n')

contatos = []

opcao_escolhida = 0

def formulario(contato: Contato):
    contato.set_nome_completo(input('Digite o nome completo: '))
    contato.set_email(input('Digite o e-mail: '))
    contato.set_numero(input('Digite o número de telefone: '))
    return contato

def inserir():
    p = Contato()
    p = formulario(p)
    p.id = len(contatos) + 1
    contatos.append(p)

def mostrar_contato():
    if len(contatos) == 0:
        print("\nNenhuma contato cadastrado.\n")
    else:
        print('\nLista de contatos\n')
        for p in contatos:
            p.exibir_contato()

def editar(contato: Contato):
    formulario(contato)

def menu():
    print('\n######################')
    print('Menu')
    print(f'1 - Novo contato \n2 - Ver contatos \n3 - Editar contato \n4 - Encerrar')
    print('######################')
    try:
        return int(input('Escolha uma opção do menu: '))
    except:
        print('Digite uma opção válida. ')

while opcao_escolhida != 4:
    opcao_escolhida = menu()
    if opcao_escolhida == 1:
        inserir()
        print('Contato cadastrado com sucesso!')
    elif opcao_escolhida == 2:
        mostrar_contato()
    elif opcao_escolhida == 3:
        if len(contatos) == 0:
            print("Não há contatos para editar.")
        else:
            mostrar_contato()
            quem_editar = int(input('Digite o código da contato que deseja editar: '))
            if quem_editar <= 0 or quem_editar > len(contatos):
                print("Código de contato inválido.")
            else:
                contato_editar = contatos[quem_editar - 1]
                editar(contato_editar)
                print('Contato editado com sucesso!')



print('Saindo...')

