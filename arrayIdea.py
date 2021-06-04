def collect():
    thing = "Hello I am going to be amazing today."

    splitList = thing.split()
    print(splitList)
    for splitIndex in range(len(splitList)):
     for stringIndex in range(len(splitList[splitIndex])):
        something = splitList[splitIndex]
        print(something[stringIndex])
    return splitList

def search(sI):
    searchValue = input('Enter a letter to search for: ')
    searchArray = [sI]
    SIZE = len(searchArray)
    counter = 0
    for i in range(SIZE):
        if searchValue == sI:
            searchArray.append(i)
            counter += i
            print(searchValue + 'was found at index:' + str(counter))
        elif searchValue != sI:
            continue
        else:
            print('search value was not found in the array')
            break
a = collect()
search(a)


