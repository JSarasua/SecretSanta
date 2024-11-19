import random

def IsValidMatch(personGiving, personReceiving, familyLists, peopleList: dict, prevMatchesList: dict):
    if personGiving == personReceiving:
        return False

    if peopleList[personGiving] != "":
        return False

    if personGiving in prevMatchesList:
        if prevMatchesList[personGiving] == personReceiving:
            return False

    for key, value in peopleList.items():
        if value == personReceiving:
            return False

    for family in familyLists:
        for person in family:
            if person == personGiving:
                for familyMember in family:
                    if personReceiving == familyMember:
                        return False

    return True

def GetRandomFamily(familyLists):
    return random.choice(familyLists)

def GetRandomPerson(familyLists):
    return random.choice(random.choice(familyLists))

def SolveSecretSanta(filepath, prevMatches):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    with open(prevMatches, "r") as openedPrevMaches:
        prevData = openedPrevMaches.readlines()

    prevMatchesList = {}
    familyLists = []
    peopleList = {}

    for prevMatch in prevData:
        if prevMatch == "\n":
            continue
        splitEntries = prevMatch.strip().split(' :  ')
        prevMatchesList[splitEntries[0]] = splitEntries[1]

    currentFamilyList = []
    for fileLine in fileData:
        if fileLine == "\n":
            familyLists.append(currentFamilyList.copy())
            currentFamilyList.clear()
        else:
            currentFamilyList.append(fileLine.strip())
            peopleList[fileLine.strip()]=""

    if len(currentFamilyList) > 0:
        familyLists.append(currentFamilyList)

    for person in peopleList:
        personReceiving = GetRandomPerson(familyLists)
        while not IsValidMatch(person, personReceiving, familyLists, peopleList, prevMatchesList):
            personReceiving = GetRandomPerson(familyLists)

        peopleList[person] = personReceiving

    for personGiving, personReceiving in peopleList.items():
        print(personGiving, ': ',personReceiving)


filePath = "C:\\dev\\misc\\family.txt"
prevMatchesPath = "C:\\dev\\misc\\prevMatches.txt"
SolveSecretSanta(filePath, prevMatchesPath)

