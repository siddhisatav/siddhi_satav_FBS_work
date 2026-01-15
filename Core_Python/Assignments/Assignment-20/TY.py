# 2. Create another package “TY” which has a class TYMarks (Theory,
# Practical).

class TYMARKS:
    def __init__(self,Theory , practical):
        self.Theory =Theory
        self.practical =practical
        
    def show(self):
        data = f"Theory : {self.Theory}/nPractical : {self.practical}"
        
        return data