import re
import random as rd
import lmstudio as lms

class Restaurant:
  def __init__(self, name, quality):
    self.name = name
    self.quality = quality
    self.rating = None

class Urb:
  def __init__(self, name, restaurants):
    self.name = name
    self.restaurants = restaurants

class Citizen:
  def __init__(self, name, model_name):
    self.name = name
    self.model = lms.llm(model_name)
    self.history = ""
    self.restaurant_pref = dict()
    for restaurant in restaurants:
      self.restaurant_pref[restaurant] = rd.choice([1, 2, 3])

  def clean_response(self, s):
    start = s.find('[')
    end = s.find(']', start)
    if start != -1 and end != -1:
        name = s[start+1:end]
        return name.replace('"', '').strip()
    return None

  def choose_restaurant(self):
    restaurant_prompt = f"""
    Your name is {self.name}. You are an inhabitant of Urbsane, a small town.
    Your goal is to pick some food to eat today. The available restaurants are:
    {str(restaurants)}

    """
    if self.history:
      restaurant_prompt += f"""Your history is:
      {self.history}

      """

    restaurant_prompt += """
    Which restaurant will you go to today? Write the name inside brackets e.g. ["Burger King"].
    Remember, you can only go to the available restaurants. 
    """

    response = self.model.respond(restaurant_prompt)
    print(response)
    choice = self.clean_response(str(response))
    today_summary = f"""
    You went to {choice} and rated it a {self.restaurant_pref[choice]} out of 5.
    """
    self.history += today_summary

    print(today_summary)


if __name__ == "__main__":
  restaurant_names = ["Salty Joe's Diner", "Carmen's", "Don Francisco's", "Borgar Joint", "Markskarnalds", "Papa Joe's!"]
  restaurants = [Restaurant(name, rd.choice(range(1,6))) for name in restaurant_names]
  for restaurant in restaurants:
    print("- " + " - "*10)
    print(restaurant.name)
    print(restaurant.quality)
    print(restaurant.rating)