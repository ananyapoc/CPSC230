def askForScore():
  x=int(input("score on test: "))
  return x

def calculateAverage():
  a = askForScore()
  b = askForScore()
  c = askForScore()
  average = (a+b+c)/3
  return average

def calculateGrade():
    avgScore = calculateAverage()
    grade = ""
    if avgScore >=90:
        grade = "A"
    elif avgScore >=80:
        grade = "B"
    elif avgScore >=70:
        grade = "C"
    else:
        grade = "F"
    return grade

print(calculateGrade())
