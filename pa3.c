#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFSIZE 256
#define TABLE_SIZE 50021

typedef struct Node {
    char word[BUFSIZE];
    struct Node* next;
} Node;

Node* hashTable[TABLE_SIZE];

unsigned int hashFunction(const char* word) {
    unsigned int hash = 5381;
    int c;
    while ((c = *word++)) {
        hash = ((hash << 5) + hash) + c;
    }
    return hash % TABLE_SIZE;
}

void insertIntoHashTable(char* word) {
    unsigned int index = hashFunction(word);
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (!newNode) {
        exit(1);
    }
    strcpy(newNode->word, word);
    newNode->next = hashTable[index];
    hashTable[index] = newNode;
}

int searchHashTable(const char* word) {
    unsigned int index = hashFunction(word);
    Node* current = hashTable[index];
    while (current) {
        if (strcmp(current->word, word) == 0) {
            return 1;
        }
        current = current->next;
    }
    return 0;
}

void freeHashTable() {
    for (int i = 0; i < TABLE_SIZE; i++) {
        Node* current = hashTable[i];
        while (current) {
            Node* temp = current;
            current = current->next;
            free(temp);
        }
    }
}

void generateSuggestions(const char* word) {
    printf("Suggestions: ");

    int wordLen = strlen(word);
    int foundSuggestion = 0;

    for (int i = 0; i < wordLen - 1; i++) {
        char temp[BUFSIZE];
        strcpy(temp, word);
        char ch = temp[i];
        temp[i] = temp[i + 1];
        temp[i + 1] = ch;
        if (searchHashTable(temp)) {
            if (foundSuggestion) printf(" ");
            printf("%s", temp);
            foundSuggestion = 1;
        }
    }

    char temp[BUFSIZE];
    if (wordLen > 1) {
        strcpy(temp, word + 1);
        if (searchHashTable(temp)) {
            if (foundSuggestion) printf(" ");
            printf("%s", temp);
            foundSuggestion = 1;
        }
        strncpy(temp, word, wordLen - 1);
        temp[wordLen - 1] = '\0';
        if (searchHashTable(temp)) {
            if (foundSuggestion) printf(" ");
            printf("%s", temp);
            foundSuggestion = 1;
        }
    }

    char extendedWord[BUFSIZE + 2];
    for (char ch = 'a'; ch <= 'z'; ch++) {
        snprintf(extendedWord, sizeof(extendedWord), "%c%s", ch, word);
        if (searchHashTable(extendedWord)) {
            if (foundSuggestion) printf(" ");
            printf("%s", extendedWord);
            foundSuggestion = 1;
        }
        snprintf(extendedWord, sizeof(extendedWord), "%s%c", word, ch);
        if (searchHashTable(extendedWord)) {
            if (foundSuggestion) printf(" ");
            printf("%s", extendedWord);
            foundSuggestion = 1;
        }
    }

    if (!foundSuggestion) {
        printf("\n");
    } else {
        printf("\n");
    }
}

int main(int argc, char **argv)
{
  char *dictionaryFilePath = argv[1]; //this keeps the path to the dictionary file file
  char *inputFilePath = argv[2]; //this keeps the path to the input text file
  char *check = argv[3]; // this keeps the flag to whether we should insert mistyped words into dictionary or ignore
  int numOfWords=0; //this variable will tell us how much memory to allocate

  int insertToDictionary;
  if(strcmp(check,"add")==0)
    insertToDictionary = 1;
  else
    insertToDictionary = 0;

  ////////////////////////////////////////////////////////////////////
  //read dictionary file
    FILE *fp = fopen(dictionaryFilePath, "r");
    char *line = NULL; //variable to be used for line counting
    size_t lineBuffSize = 0; //variable to be used for line counting
    ssize_t lineSize; //variable to be used for line counting

    //check if the file is accessible, just to make sure...
    if(fp == NULL)
    {
        fprintf(stderr, "Error opening file\n");
        exit(1);
    }

    //First, let's count number of words in the dictionary.
    //This will help us know how much memory to allocate for our hash table
    while((lineSize = getline(&line,&lineBuffSize,fp)) !=-1)
        numOfWords++;

    //Printing line count for debugging purposes.
    //You can remove this part from your submission.
    //printf("%d\n",numOfWords);

    //HINT: You can initialize your hash table here, since you know the size of the dictionary
    for (int i = 0; i < TABLE_SIZE; i++) {
        hashTable[i] = NULL;
    }

    //rewind file pointer to the beginning of the file, to be able to read it line by line.
    fseek(fp, 0, SEEK_SET);

    char wrd[BUFSIZE];
    for (int i = 0; i < numOfWords; i++)
    {
        fscanf(fp, "%s \n", wrd);
        //You can print the words for Debug purposes, just to make sure you are loading the dictionary as intended
        //printf("%d: %s\n",i,wrd);

        //HINT: here is a good place to insert the words into your hash table
        insertIntoHashTable(wrd);
    }
    fclose(fp);

  ////////////////////////////////////////////////////////////////////
  //read the input text file word by word
    fp = fopen(inputFilePath, "r");

  //check if the file is accessible, just to make sure...
  if(fp == NULL)
  {
    fprintf(stderr, "Error opening file\n");
    return -1;
  }

    //HINT: You can use a flag to indicate if there is a misspleed word or not, which is initially set to 1
  int noTypo = 1;

  //read a line from the input file
  while((lineSize = getline(&line,&lineBuffSize,fp)) !=-1)
  {
    char *word;
        //These are the delimiters you are expected to check for. Nothing else is needed here.
    const char delimiter[]= " ,.:;!\n";

    //split the buffer by delimiters to read a single word
    word = strtok(line,delimiter); 

    //read the line word by word
    while(word!=NULL)
    {
      // HINT: Since this nested while loop will keep reading the input text word by word, here is a good place to check for misspelled words
      if (!searchHashTable(word)) {
          // INPUT/OUTPUT SPECS: use the following line for printing a "word" that is misspelled
          printf("Misspelled word: %s\n", word);
          noTypo = 0;
          // INPUT/OUTPUT SPECS: use the following line for printing suggestions, each of which will be separated by a comma and whitespace.
          // printf("Suggestions: "); the suggested words should follow
          generateSuggestions(word);
          if (insertToDictionary) {
              insertIntoHashTable(word);
          }         
      }
      word = strtok(NULL,delimiter); 
    }
  }
  fclose(fp);

    //HINT: If the flag noTypo is not altered (which you should do in the loop above if there exists a word not in the dictionary), then you should print "No typo!"
    if(noTypo==1)
        printf("No typo!\n");


    // DON'T FORGET to free the memory that you allocated
    freeHashTable();

  return 0;
}