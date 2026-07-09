class Movies():
    def __init__(self , name = "zapatlela" , genre="comedy"):
        self.name = name
        self.genre = genre
        
    def getData(self):
        data = f"Name : {self.name}\nGenre:{self.genre}"
        return data
    
m1 = Movies()
print(m1.getData())

m2 = Movies('golmal' , "comedy")
print(m2.getData())

        