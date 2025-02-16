#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFSIZE 256

typedef struct item{
  char *word;
  int weight;
}Item;

void quickSort(Item arr[], int low, int high);
int partition(Item arr[], int low, int high);
int binarySearch(Item *dictionary, int wordCount, char *query);
void autocorrect(Item *dictionary, int wordCount, char *query);
void sortByFrequency(Item *arr, int count);

int main(int argc, char **argv) {
    char *dictionaryFilePath = argv[1]; //this keeps the path to dictionary file
    char *queryFilePath = argv[2]; //this keeps the path to the file that keeps a list of query wrods, 1 query per line
    int wordCount=0; //this variable will keep a count of words in the dictionary, telling us how much memory to allocate
    int queryCount=0; //this variable will keep a count of queries in the query file, telling us how much memory to allocate for the query words

    ///////////////////////////////////////////////////////////////////////////////////////////////// read dictionary file /////////////////////////////////////////////////////////////////////////////////////////////////
    FILE *fp = fopen(dictionaryFilePath, "r");
    char *line = NULL; //variable to be used for line counting
    size_t lineBuffSize = 0; //variable to be used for line counting
    ssize_t lineSize; //variable to be used for line counting

    //check if the file is accessible, just to make sure...
    if(fp == NULL){
        fprintf(stderr, "Error opening file:%s\n",dictionaryFilePath);
        return -1;
    }

    //First, let's count number of lines. This will help us know how much memory to allocate
    while((lineSize = getline(&line,&lineBuffSize,fp)) !=-1) {
        wordCount++;
    }
    free(line);
    line = NULL;

    /////////////////PAY ATTENTION HERE/////////////////
    //This might be a good place to allocate memory for your data structure, by the size of "wordCount"
    ////////////////////////////////////////////////////

    Item *knowledgeBase = malloc(wordCount * sizeof(Item));
    if (!knowledgeBase) {
        fclose(fp);
        return -1;
    }

    //Read the file once more, this time to fill in the data into memory
    fseek(fp, 0, SEEK_SET);// rewind to the beginning of the file, before reading it line by line.
    char word[BUFSIZE]; //to be used for reading lines in the loop below
    int weight;
    for(int i = 0; i < wordCount; i++) {
        fscanf(fp, "%s %d\n",word,&weight);

        /////////////////PAY ATTENTION HERE///////////////////This might be a good place to store the dictionary words into your data structure ////////////////////////////////////////////////////

        knowledgeBase[i].word = strdup(word);
        knowledgeBase[i].weight = weight;
    }
    //close the input file
    fclose(fp);

    ///////////////////////////////////////////////////////////////////////////////////////////////// read query list file /////////////////////////////////////////////////////////////////////////////////////////////////
    fp = fopen(queryFilePath, "r");

    //check if the file is accessible, just to make sure...
    if(fp == NULL) {
        fprintf(stderr, "Error opening file:%s\n",queryFilePath);
        return -1;
    }

    //First, let's count number of queries. This will help us know how much memory to allocate
    while((lineSize = getline(&line,&lineBuffSize,fp)) !=-1) {
        queryCount++;
    }
    free(line); //getline internally allocates memory, so we need to free it here so as not to leak memory!!
    line = NULL;

    /////////////////PAY ATTENTION HERE/////////////////
    //This might be a good place to allocate memory for storing query words, by the size of "queryCount"
    ////////////////////////////////////////////////////

    char **queries = malloc(queryCount * sizeof(char *));
    if (!queries) {
        fclose(fp);
        return -1;
    }

    fseek(fp, 0, SEEK_SET);// rewind to the beginning of the file, before reading it line by line.
    for(int i = 0; i < queryCount; i++) {
        fscanf(fp, "%s\n",word);

        /////////////////PAY ATTENTION HERE/////////////////
        //This might be a good place to store the query words in a list like data structure
        //////////////////////////////////////////////////// 
         queries[i] = strdup(word);
    }
    //close the input file
    fclose(fp);

    ///////////////////////////////////////////////////////////////////////////////////////////////// reading input is done ////////////////////////////////////////////////////////////////////////////////////////////////

    //Now it is your turn to do the magic!!!
    //do search/sort/print, whatever you think you need to do to satisfy the requirements of the assignment!
    //loop through the query words and list suggestions for each query word if there are any
    //don't forget to free the memory before you quit the program!

        quickSort(knowledgeBase, 0, wordCount - 1);
    
        for (int i = 0; i < queryCount; i++) {
            autocorrect(knowledgeBase, wordCount, queries[i]);
        }

        for (int i = 0; i < wordCount; i++) {
            free(knowledgeBase[i].word);
        }
        free(knowledgeBase);

        for (int i = 0; i < queryCount; i++) {
            free(queries[i]);
        }
        free(queries);

        return 0;
    }

    void quickSort(Item arr[], int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    int partition(Item arr[], int low, int high) {
        Item pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (strcmp(arr[j].word, pivot.word) < 0) {
                i++;
                Item temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        Item temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return i + 1;
    }

    int binarySearch(Item *knowledgeBase, int wordCount, char *query) {
        int left = 0, right = wordCount - 1, result = -1;
        int queryLen = strlen(query);

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (strncmp(knowledgeBase[mid].word, query, queryLen) == 0) {
                result = mid; 
                right = mid - 1;
            } else if (strcmp(knowledgeBase[mid].word, query) < 0) {
                left = mid +1;
            } else {  
                right = mid -1;
            }
        }
        return result;
    }

    void sortByFrequency(Item *arr, int count) {
        for (int i = 1; i < count; i++) {
            Item key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j].weight < key.weight) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    //OUTPUT SPECS:
    // use the following if no word to suggest: printf("No suggestion!\n");
    // use the following to print a single line of outputs (assuming that the word and weight are stored in variables named word and weight, respectively): 
    // printf("%s %d\n",word,weight);
    // if there are more than 10 outputs to print, you should print the top 10 weighted outputs.

    void autocorrect(Item *knowledgeBase, int wordCount, char *query) {
        printf("Query word:%s\n", query);
    
        int startIndex = binarySearch(knowledgeBase, wordCount, query);
        if (startIndex == -1) {
            printf("No suggestion!\n");
            return;
        }
    
        Item *matches = malloc(wordCount * sizeof(Item));
        if (!matches) return;
        
        int matchCount = 0;
        for (int i = startIndex; i < wordCount; i++) {
            if (strncmp(knowledgeBase[i].word, query, strlen(query)) == 0) {
                matches[matchCount++] = knowledgeBase[i];
            } else {
                break;
            }
        }
    
        sortByFrequency(matches, matchCount);
        for (int i = 0; i < (matchCount < 10 ? matchCount : 10); i++) {
            printf("%s %d\n", matches[i].word, matches[i].weight);
        }
    
        free(matches);
    }
