from FileLoader import Fileloader
from HowManyMedals import howManyMedals

loader = Fileloader()
data = loader.load("../resources/athlete_events.csv")

print(howManyMedals(data, 'Kjetil Andr Aamodt'))
# Output
# {1992: {’G’: 1, ’S’: 0, ’B’: 1},
# 1994: {’G’: 0, ’S’: 2, ’B’: 1},
# 1998: {’G’: 0, ’S’: 0, ’B’: 0},
# 2002: {’G’: 2, ’S’: 0, ’B’: 0},
# 2006: {’G’: 1, ’S’: 0, ’B’: 0}}
