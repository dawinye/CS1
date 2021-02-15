def create_dic():
    global dic
    file = open("Loto4.txt")
    dic = {}
    for line in file:
        line = line.strip()
        line = line.split(":")
        line = line[1][1:-1].split(",")
        for element in line:
            if element in dic:
                dic[element] +=1
            else:
                dic[element] = 1 
    print(dic)
def increasing(a):
    return a[1]

def sort():
    global dic, list1
    list1 = []
    for item in dic.items():
        list1.append(item)
        
    list1 = sorted(list1,key = increasing)[::-1]
    list2 = []
    for pair in list1:
        list2.append(pair[0])
    print(list2)
def morethanone():
    global list1
    list3 = []
    for pair in list1:
        if pair[1]>1:
            list3.append(pair[0])
    print(list3)

def neverdrawn():
    global dic
    list4 =[]
    for number in range(1,42):
        if str(number) not in dic.keys():
            list4.append(number)
    print(list4)

def most4():
    global list1, dic
    list5 = []
    list6 = []
    list7 = []
    for pair in list1:
        list6.append(pair[0])
    for pair in list1:
        list5.append(pair[1])
    i = 0
    while i < len(list5):
        if len(list7) == 4:
            break
        if list5[i] == list5[i+1]:
            if int(list6[i])> int(list6[i+1]):
                list7.append(list6[i+1])
                i+=2
            else:
                list7.append(list6[i])
                i+=2
        else:
            list7.append(list6[i])
            i+=1
        
    print(list7)

            
        
        

create_dic()
sort()
morethanone()
neverdrawn()
most4()
