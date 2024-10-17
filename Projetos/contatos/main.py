from pathlib import Path

#Define the path to the file
path_to_file = Path("contacts_list.txt")
contact_list = []

class Contact:
    def __init__(self, name, tel, email):
        self.name = name
        self.tel = tel
        self.email = email
    
    def show_contact_info(self):
        return f"Nome: {self.name}, Telefone: {self.tel}, E-mail: {self.email}"

class ContactList:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def list_contacts(self):
        for contact in self.contacts:
            print(contact.show_contact_info())
    
def main():
    contact_list = ContactList()
    while True:
        print("1. Adicione um novo contato")
        print("2. Lista de contatos")
        print("3. sair")

        choice = int(input("Selelecione a opção desejada: "))

        if choice == 1:
            print()
            print("Adicione um novo contato")
            name = str(input("Nome: "))
            tel = input("Telefone: ")
            email = str(input("E-mail: "))
            
            new_contact = Contact(name, tel, email)

            contact_list.add_contact(new_contact)

            print("Cadastrado com sucesso!")
        elif choice == 2:
            print("Lista de contatos")
            contact_list.list_contacts()

        elif choice == 3:
            print("Saindo...")
            break
        else:
            print("opção inválida, Tente novamente")

main()