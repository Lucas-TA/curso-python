from pathlib import Path

#Define the path to the file
path_to_file = Path("my_data.txt")

#Data saved to the file
data = ["Python", "C++", "Java"]

#Open the file on w (Write) mode, and save the data
with path_to_file.open(mode="w") as file:
    for item in data:
        file.write(f"{item}\n")

print("Data successfully saved!")

#Open the file on r (read) mode, and read the data
with path_to_file.open(mode="r") as file:
    data = file.readlines()

#Remove "new line" characters
data = [line.strip() for line in data]

print("Data read in the file: ", data)