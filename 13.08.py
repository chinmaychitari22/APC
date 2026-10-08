#Student Grade Management System
names = []
grades = []

def add_student():
    name = input("enter student name: ")
    grade = float(input("enter grade: "))
    names.append(name)
    grades.append(grade)
    print("student added")

def update_grade():
    name = input("enter student name: ")
    if name in names:
        index = names.index(name)
        grade = float(input("enter new grade: "))
        grades[index] = grade
        print("grade updated")
    else:
        print("student not found")

def remove_student():
    name = input("enter student name: ")
    if name in names:
        index = names.index(name)
        names.pop(index)
        grades.pop(index)
        print("student removed")
    else:
        print("student not found")

def average_grade():
    if len(grades) > 0:
        total = 0
        for i in grades:
            total += i
        print("average grade =",total/len(grades))
    else:
        print("no grades available")

def extreme_grades():
    if len(grades) > 0:
        highest = grades[0]
        lowest = grades[0]
        for i in grades:
            if i > highest:
                highest = i
            if i < lowest:
                lowest = i
        print("highest grade =",highest)
        print("lowest grade =",lowest)
    else:
        print("no grades available")

add_student()
add_student()
update_grade()
remove_student()
average_grade()
extreme_grades()


#Point Management System
def distance(p1,p2):
    x = p2[0]-p1[0]
    y = p2[1]-p1[1]
    return (x*x+y*y)**0.5

def farthest_point(points):
    farthest = points[0]
    distance1 = (points[0][0]**2+points[0][1]**2)**0.5
    for i in points:
        distance2 = (i[0]**2+i[1]**2)**0.5
        if distance2 > distance1:
            distance1 = distance2
            farthest = i
    return farthest

points = []
n = int(input("enter number of points: "))

for i in range(n):
    x = int(input("enter x: "))
    y = int(input("enter y: "))
    points.append((x,y))

p1 = points[0]
p2 = points[1]

print("distance =",distance(p1,p2))
print("farthest point =",farthest_point(points))


#Web Server Configuration
server_ip = (192,168,1,1)
allowed_ips = ["192.168.1.2","192.168.1.3"]

def update_allowed():
    ip = input("enter ip to add: ")
    allowed_ips.append(ip)

def display_config():
    print("server ip =",server_ip)
    print("allowed ips =",allowed_ips)

update_allowed()
display_config()


#Project Employee Analysis
project1 = {"Amit","Rahul","Chetan","Rohit"}
project2 = {"Chetan","Rohit","Sneha","Priya"}

print("employees in both projects =",project1.intersection(project2))
print("employees only in project 1 =",project1.difference(project2))
print("employees only in project 2 =",project2.difference(project1))
print("total unique employees =",project1.union(project2))


#Text Analysis Tool
s = input("enter paragraph: ")
words = s.split()

print("total words =",len(words))

frequency = {}

for i in words:
    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i] =1

for i in frequency:
    print(i,"=",frequency[i])

sorted_words = sorted(frequency.items(),key=lambda x:x[1],reverse=True)

print("top 3 most frequent words:")
for i in range(min(3,len(sorted_words))):
    print(sorted_words[i][0],"=",sorted_words[i][1])

vowel = 0
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="e" or i=="o" or i=="u":
        vowel +=1

print("vowels =",vowel)




