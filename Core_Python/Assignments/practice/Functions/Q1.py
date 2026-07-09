def empDetails(id , name,sal,dept):
    data = f'id:{id}\nNAME{name}\nSALARY: {sal}\nDEPT:{dept}'
    return data
result = empDetails(101,dept ="cs",name="sid",sal = 50000)
print(result)