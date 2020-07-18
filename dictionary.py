# stacgkoverflow.com/questions/2397754/how-can-i-create-an-array-list-of-dictionaries-in-python

#dictlistGOOD = list( {} for i in xrange(listsize) )  

#dictlistGOOD[0]["key"] = "value"

dictlistGOOD = list( {} for i in range(listsize) )  

dictlistGOOD[0]["key1"] = "value0"
dictlistGOOD[1]["key1"] = "value1"

for i in range(dictlistGOOD):
    print(dictlistGOOD[i])
