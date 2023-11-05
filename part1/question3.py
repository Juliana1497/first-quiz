################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

#Magical Oven
class Oven:
  def __init__(self):
    self.ingredients = []
    self.temperature = 0
    self.output = None
  
  def add(self, item):
    self.ingredients.append(item)

  def freeze(self):
    self.output = "cold"
    
  def boil(self):
    self.output = "hot"

  def wait(self):
    self.output = "neutral"
    
  def get_output(self):
    if self.output == "hot" and "lead" in self.ingredients and "mercury" in self.ingredients:
      return "gold"
    elif self.output == "hot" and "cheese" in self.ingredients and "dough" in self.ingredients and "tomato" in self.ingredients:
      return "pizza"
    elif self.output == "cold":
      return "snow"

def make_oven():
  #new instance
  return Oven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()