import copy
import random
import string

def insertionSort(array):
    for index in range(1, len(array)):
        key = array[index]
        j = index - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key

def main():
    # get user input length
    n = int(input("Input length: "))

    #generate random string from a,c,g,t
    string_input = 'acgt'
    stringToSort = ''.join((random.choice(string_input)) for x in range(n))
    print(stringToSort)

    # initialize variables
    stringSize = len(stringToSort)
    strList = []
    suffixArray = []

    print("\n=== SUFFIXES ===")
    # extract arrays in given
    for x in range(0,stringSize):
        strList.append(stringToSort[x:])
        print(f"{x}: {stringToSort[x:]}")

    duplicate = copy.deepcopy(strList)
    insertionSort(strList)

    print("\n=== SORTED ===")
    for i in range(0, len(strList)):
        # Extract current element in strList
        y = strList[i]
        # Find element in deep copy of strList
        z = duplicate.index(y)
        # Append index to suffixArray
        suffixArray.append(z)

        print(f"{z}: {y}")

    print("\n=== SUFFIX ARRAY ===")
    print(suffixArray)

main()