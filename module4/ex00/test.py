from FileLoader import Fileloader

loader = Fileloader()
data = loader.load("../resources/athlete_events.csv")
loader.display(data, 12)
