from FileLoader import Fileloader
from YoungestFellah import youngestfellah

loader = Fileloader()
data = loader.load("../resources/athlete_events.csv")

print(youngestfellah(data, 2004))
print(youngestfellah(data, 1991))
