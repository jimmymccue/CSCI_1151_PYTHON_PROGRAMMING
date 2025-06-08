"""
    City Facts
      Jimmy McCue
      The program allows a user to select a city to view facts on.
      06-08-2025
"""

user_input = ''
cities = {
  'Tokyo' : {
    'country' : 'Japan',
    'population' : '37 million',
    'fact' : 'Tokyo is the largest metropolitan area in the world and was formerly known as Edo until 1868.'
  },
  'Sao Paul' : {
    'country' : 'Brazil',
    'population' : '22 million',
    'fact' : 'São Paulo has the largest Japanese population outside of Japan.'
  },
  'Istanbul' : {
    'country' : 'Turkey',
    'population' : '16 million',
    'fact' : 'Istanbul is the only city in the world that spans two continents: Europe and Asia.'
  },
  'Whittier' : {
    'country' : 'Alaska',
    'population' : '280',
    'fact' : 'Nearly all residents of Whittier live in a single 14-story building called Begich '
    'Towers, which also houses a post office, police station, convenience store, and church. The '
    'entire town is connected through tunnels to avoid the harsh Alaskan weather.'
  },
  'Toronto' : {
    'country' : 'Canada',
    'population' : '6.8 million',
    'fact' : 'Over half of Toronto’s residents were born outside of Canada, making it one of the '
    'most multicultural cities globally.'
  },
}

while user_input != 'quit':
  print(f'To view facts about one of these cities, type the name of the city and press enter')

  for city in cities:
    print(f'{city}')

  user_input = input('Enter city or type exit and hit enter to quit:')

  for city, city_facts in cities.items():
    if user_input == city:
      print(f'{city} is a city in {city_facts['country']}')
      print(f'{city} has a population of {city_facts['population']} people')
      print(f'Fact about {city}- {city_facts['fact']}\n')
