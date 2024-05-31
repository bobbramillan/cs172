#bb3323 Bavanan Bramillan
from birthday import Birthday

def create_hash_table():
    return {i: [] for i in range(12)}

def main():
    hash_table = create_hash_table()

    while True:
        file_path = input("Enter name of the data file: ")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            break
        except FileNotFoundError:
            print("Error: that file does not exist. Try again.")

    birthday_list = []
    for line in lines:
        birthday_list.append(line.strip())

    for i, line in enumerate(birthday_list, start=1):
        cut = line.split('/')
        month = int(cut[0])
        day = int(cut[1])
        year = int(cut[2])
        bday = Birthday(month, day, year)
        hash_index = hash(bday) % 12
        hash_table[hash_index].append((bday, i))

    for index in hash_table:
        print(f"Hash location {index} has {len(hash_table[index])} elements in it.")

if __name__ == "__main__":
    main()



