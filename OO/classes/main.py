import datetime as datetime

class Person:
    # Método inicializador (__init__) é chamado quando uma nova instância da classe é criada
    def __init__(self, name, age):
        self.name = name # Atributo nome da instância recebe o valor passado ao criar o objeto
        self.age = age # Atributo idade da instância recebe o valor passado ao criar o objeto
    
    # Método para exibir informações da pessoa
    def show_info(self):
        print(f"Nome: {self.name}, Idade: {self.age}")
    
# Criando objetos da classe Person
person1 = Person("Alice", 30) # Cria uma instância da classe Person com nome 'Alice' e idade 30
person2 = Person("Pedro", 25) # Cria uma instância da classe Person com nome 'Alice' e idade 30

# Usando os métodos da classe Person
person1.show_info() # Chama o método show_info() da instância person1
person2.show_info() # Chama o método show_info() da instância person2

# Definindo a classe Car
class Car:
    # Método inicializador (__init__) é chamado quando uma nova instância da classe é criada
    def __init__(self, brand, model, year):
        self.brand = brand # Atributo brand da instância recebe o valor passado ao criar o objeto
        self.model = model # Atributo model da instância recebe o valor passado ao criar o objeto
        self.year = year # Atributo year da instância recebe o valor passado ao criar o objeto

    # Método para exibir informações do carro
    def show_info(self):
        print(f"Marca: {self.brand}, Modelo: {self.model}, Ano: {self.year}")
    
    # Método para calcular a idade do carro com base no ano atual
    def calc_years(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year

car1 = Car("Fiat", "Uno", 2008)
car1.show_info()

print(f"Este carro tem {car1.calc_years()} anos.")

class Book:
    def __init__(self, title, release_date, author):
        self.title = title
        self.release_date = release_date
        self.author = author
    
    def show_info(self):
        print(f"Título: {self.title}, Ano de lançamento: {self.release_date}, Autor: {self.author}")
    
    def calc_years(self):
        current_year = datetime.datetime.now().year
        return current_year - self.release_date

book1 = Book("Harry Potter and the Sorcery Stone", 2001, "J. K. Rowling")
book1.show_info()
print(f"Este livro tem {book1.calc_years()} anos.")