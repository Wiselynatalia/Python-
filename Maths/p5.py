#python_version == '3.7.4'
def count_alphabet(test_string):
    count=0
    for i in test_string:
        if i.isalpha() == True:
            count+=1
    return(count)

def vowel_capitalization(test_string):
    string,boolean ='',0
    vowel = ['a', 'i', 'o', 'u', 'e']
    for i in test_string:
        for x in vowel:
            if i == x:
                string += i.upper()
                boolean =0
                break
            else:
                boolean= 1
        if boolean == 1:
            string += i
    return(string)

def concat(test_string, new_string):  #apple while c<lensub count=1
    return(test_string + new_string)

def search(test_string, sub):
    ltest, lsub, j = len(test_string), len(sub), 0
    for i in range (ltest): 
        count = 0
        if test_string[i] == sub[j]:
            while(count<lsub):
                if test_string[i+count] != sub[j+count]:
                    break
                else:   
                    count+=1
                    if count == lsub:
                        return(i)
    return(-1)

def letter_count(test_string):
    x = sorted(test_string.lower())
    string, count, List, Final = " ", 1, [], []
    for i in x:
        if i.isalpha() == True:
            List.append(i)
    for i in range (len(List)-1):
        if List[i] == List[i+1]:
            count +=1
            if i == len(List)-2:
                tup =(List[len(List)-1], count)
                Final.append(tup)
        else:
            tup = (List[i],count)
            Final.append(tup)
            count=1
            if i == len(List)-2:
                tup =(List[len(List)-1], count)
                Final.append(tup)
    return(Final)





