from person import Person

people = []

choose_option = 0

    

def form(person: Person):
    person.set_name(input('Digite o nome '))
    person.set_number(input('Digite o numero de telefone '))
    return person

def insert():
    p = Person()
    p = form(p)
    p.id = len(people) + 1
    people.append(p)

def show_people():
    if len(people) == 0:
        print("\nNenhuma pessoa cadastrada.\n")
    else:
        print('\nLista de pessoas \n')
        for p in people:
            p.to_string()

def edit(person: Person):
    form(person)
    

def menu():
    print('\nMenu')
    print(f'1 - Nova pessoa \n2 - Ver pessoas \n3 - Editar pessoa \n4 - Encerrar\n')
    try:
        return int(input('Escolha uma opção do menu: '))
    except:
        print('Digite uma opção válida. ')


while choose_option != 4:
    choose_option = menu()
    if choose_option == 1:
        insert()
    elif choose_option == 2:
        show_people()
    elif choose_option == 3:
        who_to_edit = int(input('Digite o código dá pessoa que deseja editar: '))
        to_edit_person = people[who_to_edit - 1]
        edit(to_edit_person)
        
