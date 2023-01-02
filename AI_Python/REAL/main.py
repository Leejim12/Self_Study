from problem import *
from optimizer import *

def main():
  p,pType = selectProblem()
  alg = selectAlgorithm(pType)
  alg.run(p)
  p.describe()
  alg.displaySetting()
  p.report()
  
def selectProblem():
  print("Select the problem type:")
  print("1. Numerical Optimization")
  print("2. TSP")
  pType = int(input("Enter the number :"))
  # pType = 2
  
  if pType == 1:
    p = Numeric()
  elif pType == 2:
    p = Tsp()
  p.setVariables()
  return p,pType

def selectAlgorithm(pType):
  print()
  print("Select the search algorithm:")
  print("1. Steepest-Ascent")
  print("2. First-Choice")
  print("3. Gradient Descent")
  print("4. stochastic")
  while True:
    aType = int(input("Enter the number"))
    if not invalid(pType,aType):
      break
  optimizers = {
    1: 'SteepestAscent()',
    2: 'FirstChoice()',
    3: 'GradientDescent()',
    4: 'stochastic()',
  }
  alg = eval(optimizers[aType])
  alg.setVariables(pType)
  return alg

def invalid(pType,aType):
  if pType == 2 and aType == 2 :
    print("You cannot choose")
    print("unless ur ~~")
    return True
  else:
    return False
  
main()
    