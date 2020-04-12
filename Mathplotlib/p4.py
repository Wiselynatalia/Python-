#python_version == '3.7.4'
def get_average_grades(filename='grades.csv'):
    Sum, List, student, Avg, x= 0, [], 0, [], 0
    with open(filename) as file:
        for line in file:
            List.append((line.rstrip("\n").split(","))) 

    for x in range (0,len(List[0])):
        for i in range (0, len(List)):
            if float(List[i][x]) != -1:
                Sum += float(List[i][x])
                student +=1
        Avg.append(Sum/student)
        Sum,student=0,0
    return(Avg)
            