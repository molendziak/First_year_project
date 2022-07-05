from matplotlib import pyplot as plt
from math import sin
from math import pi
from math import cos

from functions import correctFile
from functions import makeAverageList
from functions import plotlist
from functions import plotWith2BandsError






correctFile('J:\\Physics\\Teaching\\spa4601\\ProjectData\\Data.monthly_nh.txt','NH.Corrected')



makeAverageList('NH.Corrected', 1,2,48)

a = makeAverageList('NH.Corrected', 1,2,48)

plotlist('test',a,)

makeAverageList('NH.Corrected', 1,2,12)


c = makeAverageList('NH.Corrected', 1,2,12)

plotlist('test',c,)


makeAverageList('NH.Corrected', 1,2,6)


b = makeAverageList('NH.Corrected', 1,2,6)

plotlist('test',b,)

nomList = makeAverageList('NH.Corrected', 1, 2, 48)
errorList1 = makeAverageList('NH.Corrected', 9, 10, 48)
errorList2 = makeAverageList('NH.Corrected', 11, 12, 48)
plotWith2BandsError('Clay','test.png',nomList,errorList1,errorList2)

