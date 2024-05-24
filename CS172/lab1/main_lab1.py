#Bavanan Bramillan bb3323
#program checks txt files for words of correct spelling in each line

from spellchecker import *

#this function asks user to imput a valid file
def get_file():
    while True:
        name_file = input("Enter the name of the file to read: ")
        try:
            f = open(name_file, "r")
            return f
        except FileNotFoundError:
                print("Could not open file.")


if __name__ == "__main__":
    print("Welcome to Text File Spellchecker.")
    file = get_file() 
    
    SP = Spellchecker("english_words.txt")

    line_number = 0
    words_correct = 0
    words_failed = 0
    for line in file:
        words = line.split()
        line_number+=1
        for word in words:
            if SP.check(word) == True:
                words_correct+=1
            else:
                words_failed+=1
                print(f'Possible Spelling Error on line {line_number}: {word}')
    
    print(f'{words_correct:,} words passed spell checker.')
    print(f'{words_failed:,} words failed spell checker.')

    percentage_words = words_correct/(words_correct+words_failed) * 100

    print(f'{percentage_words:.2f}% of words passed.')







