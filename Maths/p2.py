#python_version == '3.7.4'
def roman_to_decimal(str):       
    lstr = len(str)
    n = 0
    for i in range (lstr):
        dictroman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for x in (dictroman):
            if i < (lstr -1) :
                if str[i] == "I" and (str[i+1] =="V" or str[i+1]=="X") :
                    if str[i] == x:
                        n -= dictroman[x]
                elif str[i] == "X" and (str[i+1] =="L" or str[i+1]=="C") :
                    if str[i] == x:
                        n -= dictroman[x]
                elif str[i] == "C" and (str[i+1] =="D" or str[i+1]=="M") :
                    if str[i] == x:
                        n -= dictroman[x]
                elif str[i] == x:
                    n += dictroman[x]
            else:
                if str[i] == x:
                    n += dictroman[x]
    return n
