from FileLoader import Fileloader
from HowManyMedalsByCountry import howManyMedalsByCountry
loader = Fileloader()
data = loader.load("../resources/athlete_events.csv")

print(howManyMedalsByCountry(data, 'United Arab Emirates'))
# output
# {2192: {’G’: 17, ’S’: 14, ’B’: 23}
#  2196: {’G’: 8, ’S’: 21, ’B’: 19},
#  2200: {’G’: 26, ’S’: 19, ’B’: 7}}
