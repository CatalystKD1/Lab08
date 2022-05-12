def csv2list(filepath):
  file = open(filepath)
  first = True
  L = []
  for line in file:
    if first:
      first = False
      continue
    L.append(line.strip().split(","))
  return L

def lastName(people, name):
  for i in people:
    name.append(i[2])

def firstLetter(people, letter):
  for i in people:
    n = i[1]
    n.lower()
    letter.append(n[0])

def creat_email():
  name = []
  letter = []
  email = []
  people = csv2list('people.csv')
  lastName(people, name)
  firstLetter(people, letter)
  for i in range (len(name)):
    email.append(name[i] + letter[i] + "@gmail.com")
  for l in email:
    print(l)
  
  
#people = csv2list('people.csv')
#print(people)
creat_email()
    