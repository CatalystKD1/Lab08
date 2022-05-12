import os
def getInt(message):
  temp = 0
  while(True):
    try:
      temp = int(input(message))
      break
    except:
      print("That is not the proper value.")
  return temp
  
def getStr(message):
  while(True):
    temp = input(message)
    try:
      temp = int(temp)
      print("That is not the proper value.")
    except:
      temp.lower
      break
  return temp

def addStudent(studentClass, studentAvr):
  temp = []
  studentName = getStr("What is the students name?")
  studentGrade = getInt("What is the students grades?")
  studentAvr.append(studentGrade)
  temp.append(studentName)
  temp.append(studentGrade)
  studentClass.append(temp)

def removeStudent(studentClass, studentAvr):
  # I need to get the grade value and remove it from studentAvr
  while True:
    #I had a plan for this. Not using it anymore
    temp = []
    answer = getStr("Would you like to see the sutdents? Y or N.")
    if(answer == "y"):
      print(studentClass)
    studentName = getStr("What is the students name?")
    studentGrade = getInt("What is the students grades?")
    temp.append(studentName)
    temp.append(studentGrade)
    if temp in studentClass:
      studentClass.remove(temp)
      studentAvr.remove(studentGrade)
      break
    else:
      print("That student is not in the lsit. Returning you to the menu.")
      print("")
      break

def classAvr(studentAvr):
  x = 0
  for i in range (len(studentAvr)):
    x += studentAvr[i]
  avr = x / len(studentAvr)
  print(f"This classes student averag is {avr}.")
  
def menu(studentClass, studentAvr):
  answer = "a"
  while answer != "quit":
    print("Add student = 'add'.")
    print("Remove student = 'remove'.")
    print("Average of students = 'avr'.")
    print("Quit = 'quit'.")
    answer = getStr("")
    if answer == "add":
      addStudent(studentClass, studentAvr)
      continue
    elif (answer == "remove"):
      if(len(studentClass) == 0):
        print("There are no students to remove")
      else:
        removeStudent(studentClass, studentAvr)
    elif (answer == "avr"):
      print("yo")
      classAvr(studentAvr)
    elif(answer == "quit"):
      print("Have a nice day.")
      break
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("That is no the correct command. Try again.")
      print("")
    print(studentClass)
      

studentClass = []
studentAvr = []
menu(studentClass, studentAvr)