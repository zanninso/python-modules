from MyPlotLib import MyPlotLib
from FileLoader import Fileloader
import pdb

loader = Fileloader()
data = loader.load("../resources/athlete_events.csv")
MyPlotLib().histogram(data, ["Height", "Weight"])
MyPlotLib().density(data, ["Weight", "Height"])
MyPlotLib().pair_plot(data, ["Weight", "Height"])
MyPlotLib().box_plot(data, ["Weight", "Height"])
