#bb3323 Bavanan Bramillan
#compares the search length of a list to a Binary Search Tree and 
#populates the list and converts list to BST to compare the og list to BST

import random
from BST import BST

def populateList(n):
    ##TODO: implement your logic here
    lst = []

    for i in range(0, n):
        lst.append(i)

    random.shuffle(lst)
    return lst

def searchLength(lst, n):
    elem = 0

    for x in lst:
        if x != n:
            elem+=1
        elif x == n:
            break  
    return elem
        
def listToBST(lst):
    bst = BST()
    for elem in lst:
        bst.append(elem)
    return bst

if __name__ == "__main__":
    ##TODO: implement your logic here
    avg_list = []
    avg_bst = []

    for n in range(1, 1000, 100):
        sumcountlist = 0
        sumcountbst = 0
        numruns = 0

        for s in range (1, 5):
            lst = populateList(n)
            bst = listToBST(lst)

            for v in range(n):
                sumcountlist += searchLength(lst, v)
                sumcountbst += bst.searchLength(v)
                numruns += 1

        avg_list.append(round(sumcountlist/numruns))
        avg_bst.append(round(sumcountbst/numruns))


    print(f"Average Search Length for List: {avg_list}")
    print(f"Average Search Length for BST: {avg_bst}")