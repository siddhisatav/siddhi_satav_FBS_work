def common_element(list1,list2):
    dict={}
    count=0
    for i in list1:
        dict[i]=1
    common=[]
    for j in list2:
        if dict.get(j) != None:
            print(j)
            count+=1
   