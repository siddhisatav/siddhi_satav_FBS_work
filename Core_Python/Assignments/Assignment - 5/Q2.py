# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
no_of_student = int(input("enter number of student : "))


all_percentage = []

for i in range(1,no_of_student+1):
      print("Marks of student ", i )
      Sub_1 = int(input("Enter marks of subject 1 : "))
      Sub_2 = int(input("Enter marks of subject 2 :"))
      Sub_3 = int(input("Enter marks of subject 3 :"))
      Sub_4 = int(input("Enter marks of subject 4 :"))
      Sub_5 = int(input("Enter marks of subject 5 : "))
     
      percentage= ((Sub_1+Sub_2+Sub_3+Sub_4+Sub_5)/500) * 100
      all_percentage.append(percentage)
      
      print(f" \n percentage of student {i}: {percentage}% \n")
      
      
print("----- All Students Percentage -----")
for i in range (len(all_percentage)):
      print(f"Students percentage {i+1} : {all_percentage[i]}%")
      
average_percentage= sum(all_percentage)/no_of_student
print(f"Average percentage of all students : {average_percentage}%")

