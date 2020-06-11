def mergewords(input1,input2):
    
    input1 = list(input1)
    input2 = list(input2)

    newword = []

    for i in range(len(input1)):
            newword.append(input1[i])
            newword.append(input2[i])
            
    return "".join(newword)


