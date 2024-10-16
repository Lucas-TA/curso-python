#projeto lojinha

def register_customer(name, email, tel):
    with open("customers.txt", "a") as f:
        f.write(f"{name},{email},{tel}\n")
    print("Registered successfully!")

def list_customers():
    try:
        with open("customers.txt", "r") as f:
            customers = f.readlines()
            if not customers:
                print("No customers found!")
                return
            else:
                print("Registered Customer List")
                for customer in customers:
                    name, email, tel = customer.strip("\n").split(",")
                    print(f"Nome: {name}, E-mail: {email},Tel  : {tel}")
    except FileNotFoundError:
        print("No customers file found!")

#Handle files
def store_data(data, file_name):
    with open(file_name, "w") as f:
        for data in data:
            f.write(f"{data}\n")
#Read files
def read_files(file_name):
    try:
        with open(file_name, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

#test
register_customer("Fulano", "fulanodasilva@teste.com", "11987876565")
register_customer("Ciclano", "ciclanodasilva@teste.com", "11943432233")
list_customers()