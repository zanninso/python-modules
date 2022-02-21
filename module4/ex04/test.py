from FileLoader import Fileloader
from SpatioTemporalData import SpatioTemporalData

loader = Fileloader()
data = loader.load("../resources/athlete_events.csv")

sp = SpatioTemporalData(data)
print(sp.where(1896))
# Output
# [’Athina’]
print(sp.where(2016))
# Output
# [’Rio de Janeiro’]
print(sp.when('Athina'))
# Output
# [2004, 1906, 1896]
print(sp.when('Paris'))
# Output
# [1900, 1924]
