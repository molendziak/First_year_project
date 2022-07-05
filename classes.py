from matplotlib import pyplot as plt
from math import sin
from math import pi
from math import cos

class Analysis:
    def __init__(self, xtitle='x', ytitle='y', inputfiles = [], titles = []):
        def addfile(self):
            self.inputfiles.append(str(input('input file')))
            self.titles.append(str(input('title')))
        def printall(self):
            print('\n input file:',self.inputfiles)
            print('\n title:', self.titles)

