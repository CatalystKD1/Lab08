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

def getCountry(people):
  country = []
  for i in people:
    country.append(i[4])
  country.sort()
  return country

def country_count(country):
  #12
  countryTimes = []
  times = 1
  while (len(country) != 0):
    c = []
    # i need to add times is appears and what country
    c.append(country[0])
    temp = country[0]
    country.remove(temp)
    while True:
      if(temp not in country):
        break
      times += 1
      country.remove(temp)
    c.append(times)
    countryTimes.append(c)
    if len(country) == 0:
      break
  return(countryTimes)

def countries():
  people = csv2list('people.csv')
  country = getCountry(people)
  countryTimes = country_count(country)
  print("Each country and number of people thast originate in those counties are:")
  for i in countryTimes:
    print(i)
  
#people = csv2list('people.csv')
#print(people)
countries()
    