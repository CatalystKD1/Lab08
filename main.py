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

def countries():
  people = csv2list('people.csv')
  
  
#people = csv2list('people.csv')
#print(people)
countries()
    