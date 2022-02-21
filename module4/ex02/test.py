
from FileLoader import Fileloader
from ProportionBySport import proportionBySport
import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)


loader = Fileloader()
data = loader.load("../resources/athlete_events.csv")

print(proportionBySport(data, 2004, 'Tennis', 'F'))
