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
class oven:
  def __init__( ingredients, temperature):
    self.ingredients = ingredients
    self.temperature = temperature
  
  def add(item):
    return item

  def freeze():
    ingredients = None
    if ingredients == ["water", "air"]:
      return "snow"
    
  def boil():
    ingredients = None
    if ingredients == ["lead", "mercury"]:
      return "gold"
    
  def get_output():
    ingredients = None
    temperature = 0
    if ingredients == ["water", "air"] and temperature<0:
      return "snow"   
    if ingredients == ["lead", "mercury"] and temperature >= 100:
      return "gold"
    if ingredients == ["cheese", "dough", "tomato"] and temperature >= 100:
      return "pizza" 

def make_oven():
  o1 = oven([],0)

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