from matplotlib import pyplot as plt
from math import sin
from math import pi
from math import cos

from functions import correctFile
from functions import makeAverageList
from functions import plotlist
from functions import plotWith2BandsError


str1 = 'J:\\Physics\\Teaching\\spa4601\\ProjectData\\Data.monthly_tropical.txt'
str2 = 'TROPICAL.Corrected'

correctFile('J:\\Physics\\Teaching\\spa4601\\ProjectData\\Data.monthly_nh.txt','NH.Corrected')
correctFile('J:\\Physics\\Teaching\\spa4601\\ProjectData\\Data.monthly_sh.txt','SH.Corrected')
correctFile('J:\\Physics\\Teaching\\spa4601\\ProjectData\\Data.monthly_ns.txt','NS.Corrected')
correctFile(str1,str2)
makeAverageList('NH.Corrected', 1,2,48)
#plotlist('test',makeAverageList('NH.Corrected', 1,2,48) )
nomListSH = makeAverageList('SH.Corrected', 1, 2, 48)
errorList1SH = makeAverageList('SH.Corrected', 9, 10, 48)
errorList2SH = makeAverageList('SH.Corrected', 11, 12, 48)
plotWith2BandsError('SH over 48 months','A3part2c.png',nomListSH,errorList1SH,errorList2SH)

nomListNS = makeAverageList('NS.Corrected', 1, 2, 48)
errorList1NS = makeAverageList('NS.Corrected', 9, 10, 48)
errorList2NS = makeAverageList('NS.Corrected', 11, 12, 48)
plotWith2BandsError('NS over 48 months','A3part2d.png',nomListNS,errorList1NS,errorList2NS)

nomListTROPICAL = makeAverageList('TROPICAL.Corrected', 1, 2, 48)
errorList1TROPICAL = makeAverageList('TROPICAL.Corrected', 9, 10, 48)
errorList2TROPICAL = makeAverageList('TROPICAL.Corrected', 11, 12, 48)
plotWith2BandsError('TROPICAL over 48 months','A3part2e.png',nomListTROPICAL,errorList1TROPICAL,errorList2TROPICAL)

nomListNH = makeAverageList('NH.Corrected', 1, 2, 48)
errorList1NH = makeAverageList('NH.Corrected', 9, 10, 48)
errorList2NH = makeAverageList('NH.Corrected', 11, 12, 48)
plotWith2BandsError('NH over 48 months','A3part2b.png',nomListNH,errorList1NH,errorList2NH)
