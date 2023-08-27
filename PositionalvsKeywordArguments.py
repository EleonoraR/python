#positional arguments
def greet_with(name,location):
  print(f"Hello {name}")
  print(f"Are you from {location}?")

greet_with("Angela","Lviv")
greet_with("Toronto","Pam")

#keyword arguments
greet_with(name="Angela",location="Paris")
greet_with(location="Paris",name="Angela")
