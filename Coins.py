import random

class Coin:
  def __init__(self, rare=False,clean=True, heads = True, **kwargs):
    #take all attributes from child class dictionary and implement
    for key,value in kwargs.items():
      setattr(self,key,value)

    self.is_rare = rare
    self.is_clean = clean
    self.heads = heads
    #determine if the coin is rare *add 25% if yes
    if self.is_rare:
      self.value = self.value * 1.25
    else:
      self.value = self.origional_value

    #determine if origional coin is clean / rusty
    if self.is_clean:
      self.color = self.clean_color
    else:
      self.color = self.rusty_color

  #Gives the coin a rusty color
  def rust(self):
    self.color = self.rusty_color

  #General cleaning of coin / changes color
  def clean(self):
    self.color = self.clean_color

  #Destructor Method
  def __del__ (self):
    print("coin spent!")

  #random function to flip
  def flip(self):
    heads_options = [True,False]
    choice = random.choice(heads_options)
    self.heads = choice

  def __str__(self):
    if self.origional_value >= 1:
      return "{} Pound coin".format(int(self.origional_value))
    else:
      return "{} pence coin".format(int(self.origional_value * 100))

#First coin as child class
class One_Pound(Coin):
  def __init__(self):
    data = {
      "origional_value": 1.00,
      "clean_color": "gold",
      "rusty_color": "greenish",
      "num_edges": 1,
      "diameter": 22.5,
      "thickness":3.15,
      "mass": 9.5
    }
    super().__init__(**data)

#Second Coin as Child class
class One_Pence(Coin):
  def __init__(self):
    data = {
      "origional_value": 0.01,
      "clean_color": "bronze",
      "rusty_color": "brownish",
      "num_edges": 1,
      "diameter": 20.3,
      "thickness":1.52,
      "mass": 3.56
    }
    super().__init__(**data)

#Third Coin as Child class
class Two_Pence(Coin):
  def __init__(self):
    data = {
      "origional_value": 0.02,
      "clean_color": "bronze",
      "rusty_color": "brownish",
      "num_edges": 1,
      "diameter": 25.9,
      "thickness":1.85,
      "mass": 7.12
    }
    super().__init__(**data)

#Fourth Coin as Child class
class Five_Pence(Coin):
  def __init__(self):
    data = {
      "origional_value": 0.05,
      "clean_color": "silver",
      "rusty_color": None,
      "num_edges": 1,
      "diameter": 18.0,
      "thickness":1.77,
      "mass": 3.25
    }
    super().__init__(**data)

    def rust(self):
      self.color = self.clean_color

    def clean(self):
      self.color = self.clean_color

#Fifth coin as child class
class Ten_Pence(Coin):
  def __init__(self):
    data = {
      "origional_value": 0.10,
      "clean_color": "silver",
      "rusty_color": None,
      "num_edges": 1,
      "diameter": 24.5,
      "thickness":1.85,
      "mass": 6.50
    }
    super().__init__(**data)

    def rust(self):
      self.color = self.clean_color

    def clean(self):
      self.color = self.clean_color

#Sixth coin as child class
class Twenty_Pence(Coin):
  def __init__(self):
    data = {
      "origional_value": 0.20,
      "clean_color": "silver",
      "rusty_color": None,
      "num_edges": 7,
      "diameter": 21.4,
      "thickness":1.7,
      "mass": 5.00
    }
    super().__init__(**data)

    def rust(self):
      self.color = self.clean_color

    def clean(self):
      self.color = self.clean_color

#Seventh coin as child class
class Fifty_Pence(Coin):
  def __init__(self):
    data = {
      "origional_value": 0.50,
      "clean_color": "silver",
      "rusty_color": None,
      "num_edges": 7,
      "diameter": 27.3,
      "thickness":1.78,
      "mass": 8.00
    }
    super().__init__(**data)

    def rust(self):
      self.color = self.clean_color

    def clean(self):
      self.color = self.clean_color

class Two_Pound(Coin):
  def __init__(self):
    data = {
      "origional_value": 2.00,
      "clean_color": "gold & silver",
      "rusty_color": "greenish",
      "num_edges": 1,
      "diameter": 28.4,
      "thickness":2.50,
      "mass": 12.00
    }
    super().__init__(**data)


coins = [One_Pence(),Two_Pence(),Five_Pence(),Ten_Pence(),
Twenty_Pence(),Fifty_Pence(),One_Pound(), Two_Pound()]

for coin in coins:
  arguments = [coin,coin.color,coin.value,coin.diameter,                    coin.thickness,coin.num_edges,coin.mass]
  string = "{} - color: {}, value: {}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{} ".format(*arguments)

print(string)


coin1 = One_Pound()
int(coin1.color)
print(coin1.num_edges)
coin1.rust()
print(coin1.color)
