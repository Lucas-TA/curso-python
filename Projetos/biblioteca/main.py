#projeto da Biblioteca com Classes

"""__Classes__

Book. Para representar os livros da biblioteca

Library. Para gerenciar os livros, permitindo adicionar, listar e salvar em arquivos textos.

"""
from pathlib import Path

path_to_file = Path("./book_list.txt")

class Book:
    def __init__(self, title, release_year, author):
        self.title = title
        self.release_year = release_year
        self.author = author
    
    def show_info(self):
        return f"Titulo: {self.title}, Ano de Lançamento: {self.release_year}, Autor(a): {self.author}"
    
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def consult_books(self, save_to_file=False):
        if save_to_file:
            with path_to_file.open(mode="w") as f:
                for book in self.books:
                    f.write(f"{book.show_info()}\n")
            print("Lista de livros salva com sucesso!")
        else:
            for book in self.books:
                print(book.show_info())
def main():
    library = Library()

    while True:
        print(f"Welcome to the Library\n")
        print("1. Add a new book to the list.")
        print("2. Consult the Book List.")
        print("3. Salvas alterações.")
        print("4. Sair.")

        choice = int(input("Please, choose one of the options above to continue: "))

        if choice == 1:
            print()
            print("New Book")

            title = str(input("Book title: "))
            release_year = int(input("Ano de lançamento: "))
            author = str(input("Autor: "))

            book = Book(title, release_year, author)
            library.add_book(book)

            print("Livro adicionado com sucesso!")
        elif choice == 2:
            print()
            print("Lista de livros:")
            library.consult_books()
        elif choice == 3:
            print("Salvando lista de livros no arquivo...")
            library.consult_books(save_to_file=True)
        elif choice == 4:
            print("Saindo...")
            break
        else:
            print("opção inválida, Tente novamente")

main()



