#python_version == '3.7.4'
def non_unique(List):
    lenl = len(List)
    final, boolean = [], 0
    for i in range (0,lenl-1):
        for j in range (i+1,lenl):
            if List[i] == List[j] and List[i]!=" ":
                List[j] = " "
                boolean =1
        if boolean ==1 and List[i]!=" ":
            final.append(List[i])
            boolean = 0
    return(final)

