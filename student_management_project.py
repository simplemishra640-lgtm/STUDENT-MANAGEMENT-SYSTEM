import json
try:
    with open("students.json","r") as file:
        students=json.load(file)
except FileNotFoundError:
    students={
        101:{
            "name":"rahul","marks":90
            },
        102:{
            'name':"rahu","marks":85
            },
        103:{
            "name":"priya","marks":98
            }
        }
while True:
    print("==========student marks management system==========")
    print("1.add student")
    print("2.view students")
    print("3.search student")
    print("4.update marks")
    print("5.delete student")
    print("6.exit")
    try:
        c=int(input('enter your choice in number(1-6)'))
    except ValueError:
        print("please add a number between 1 to 6")
        continue
    if c==1:
        student_id=int(input("enter student id"))
        name=input("enter student name")
        if student_id in students:
            print("student already exist")
        else:
            marks=int(input("enter student marks"))
            if 0<= marks <= 100:
                students[student_id]={
                    "name":name,
                    "marks":marks
                }
                print("student added successfully")
            else:
                print("marks must be between 0 to 100")
    elif c==2:
        print("students list")
        for key,value in sorted (students.items(),key=lambda item:item[1]["marks"],reverse=True):
            print(key,":",value)
    elif c==3:
        student_id=int(input("enter student id"))
        if student_id in students:
            print("name:",students[student_id]['name'])
            print("marks:",students[student_id]['marks'])
        else:
            print("student not found")
    elif c==4:
        student_id=int(input("enter student id"))
        if student_id in students:
            marks=int(input("enter new marks"))
            students[student_id]["marks"]=marks
            print("marks updated successfully")
        else:
            print("student not found")
    elif c==5:
        student_id=int(input("enter student id"))
        if student_id in students:
            del students[student_id]
            print("student data deleted successfully")
        else:
            print("student not found")
    elif c==6:
        with open('students.json','w')as file:
            json.dump(students,file)
            print("thank you!")
            break
    else:
        print("invalid choice")








    







