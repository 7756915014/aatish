''' a name is just a label for an object  and each object has lots of name 
we have diffrent types of objects 
simple :- numbers, string
contener objects:- dict, list, user defind, classes
what is refrence :- a name or container object pointing at another object
the del statement dosent delet object  it removes that name as eference to that object
every python objects holds 3 things 
its type
its value
a refrence count


'''
'''
def print_word():
    word= "seven"
    print("word is" + word)
print_word()

x= 300
y = 300
z = 300
print(id(x))
print(id(y))
print(x is y, z)
a = 300
a = 0

print(a)
a=3
b=a
c=b
d=c
print(d)
'''

roll_no = int(input("enter your roll nomber:  "))
student_name = input("enter Name: ")
gender = input("enter gender")
clas= int(input("enter class"))
english = int(input("enter english marks: "))
physics = int(input("enter physics marks: "))
chemistry = int(input("enter chemistry marks: "))
biology = int(input("enter biology marks: "))
maths = int(input("enter maths marks: "))
hindi = int(input("enter hindi marks: "))


obtained_marks = english + physics + chemistry + biology + maths + hindi
print(" obtained marks ", obtained_marks)
percentage = obtained_marks/600*100

print("------------------------STUDENT'S MARKSHEET--------------------------")
print("your roll number is:  " , roll_no )
print("your name is: " + student_name )
print("your gender is:   " + gender)
print("your gender is:m", clas)
print("your percentage is", percentage)
#print("------------------------CONGRATULATIONS YOU ARE PASS------------------------")



if percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: A")
elif  percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
elif  percentage >= 35:
    print("Grade: E")
else:
    print("fail")
i = 0

student_subject = []
if english <= 33:
    i+= 1
    student_subject.append("english")
if physics <= 33:
    i+= 1
    student_subject.append("physics")
if chemistry <= 33:
    i+= 1
    student_subject.append("chemistry")

    
if maths <= 33:
    i+= 1
    student_subject.append("maths")
if hindi <=33:
    i+=  1
    student_subject.append("hindi")
print("Failed student count: ", i)
print("Failed Subjects name: " , *(student_subject))










