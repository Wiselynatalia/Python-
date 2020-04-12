#python_version == '3.7.4'
def divisible_sublist(list1, d1, d2):
    lista = [i for i in (list1) if int(i) % d1 == 0 or int(i)%d2 ==0]
    listb = [i for i in (list1) if int(i) % d1 == 0 and int(i)%d2 ==0]
    listc = [i for i in (list1) if int(i) % d1 != 0 and int(i)%d2 !=0]
    return lista, listb, listc

