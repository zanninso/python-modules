from Komparator import Komparator
from FileLoader import Fileloader
import pdb

loader = Fileloader()
data = loader.load("../resources/athlete_events.csv")
kmp = Komparator(data)
kmp.compare_histograms('Sex', 'Height')
kmp.density('Sex', 'Height')
kmp.compare_box_plots('Sex', 'Height')
