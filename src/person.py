class Person:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.number = ''

    def set_name(self, name: str):
        if name: 
           self.name = name


    def set_number(self, number: str):
       if number:
           self.number = number

    def to_string(self):
        print(f'\nID: {self.id} \n  Nome: {self.name}\n  Telefone: {self.number}')
