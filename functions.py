from matplotlib import pyplot as plt
from math import sin
from math import pi
from math import cos


def correctFile(fileInput,fileOutput):
    li = []
    f = open(fileInput, 'r')
    h = open(fileOutput,'w')
    h.write('')
    for line in range(0, 2037):
        x = f.readline()
        x = x.strip("\n")
        li = x.split(" ")
        lis = list(filter(None,li))
        year = lis[0].split('/')
        integeryear = year[0]
        floatyear = f"{((float(int(year[0])+float(year[1])/12))):.2f}"
        nyear = [integeryear,floatyear]
        data = []
        del lis[0]

        for val in lis:
            nyear.append(val)

        nyear[12].rstrip("\n")

        r = open(fileOutput, 'a')
        r.write(str(int(nyear[0]))+','+str(float(nyear[1]))+','+str(float(nyear[2]))+','+str(float(nyear[3]))+','+str(float(nyear[4]))+','+str(float(nyear[5]))+','+str(float(nyear[6]))+','+str(float(nyear[7]))+','+str(float(nyear[8]))+','+str(float(nyear[9]))+','+str(float(nyear[10]))+','+str(float(nyear[11]))+','+str(float(nyear[12])))

        r.write("\n")



def makeAverageList(string,in1=1,in2=2,in3=12):
    f = open(string, 'r')
    averageList = []
    a = 0
    c = in3
    suma = 0
    sumb = 0
    for line in f.readlines():
        x = line.split(',')
        a = a+1
        suma += float(x[in1])
        sumb += float(x[in2])
        if a == c:
            averageList.append((suma/in3, sumb/in3))
            suma = 0
            sumb = 0
            c += in3
    #print(averageList)
    return averageList

   # list = []
   # for n in range(0,len(averageli)):
   #     tu = (averageli[n],averagelis[n])
   #     list.append(tu)
   # a = int(2037/in3)
    #averageli = []
    #or i in range(0, len(li), i3):
    #    list(chain.from_iterable([mean(li[i:i+i3])]))*i3
    #for i in range(0,a):
    #tu = (float((li[i])/i3),(float(lis[i]/i3))

        #list.append(tu)
    #print(list)
 #   return(list)





#makeAverageUpErrorList(r'C:\Users\ap19062\SPA4601\PyCharmProjects\clay-and-mateusz-project\A3.2\Output')

#makeAverageDownErrorList(r'C:\Users\ap19062\SPA4601\PyCharmProjects\clay-and-mateusz-project\A3.2\Output')

def plotWith2BandsError(namePlot,untype,tupleList,tuplesError1,tuplesError2,colorCurve='k',colorError='r',Xtitle='X',Ytitle='Y'):
    if len(tupleList) != len(tuplesError1):
        print('Lengths of lists of data points are not equal')
        exit()
    if len(tupleList) != len(tuplesError2):
        print('Lengths of lists of data points are not equal')
        exit()
    if len(tuplesError1) != len(tuplesError2):
        print('Lengths of lists of data points are not equal')
        exit()
    g = tupleList
    res = [[i for i, j in g], [j for i, j in g]]
    x = res[0]
    y = res[1]
    h = tuplesError1
    k = tuplesError2
    error1 = [[i for i, j in h], [j for i, j in h]]
    uperror1 = error1[0]
    downerror1 = error1[1]
    error2 = [[i for i, j in k], [j for i, j in k]]
    uperror2 = error2[0]
    downerror2 = error2[1]



    #downerrorxy = [[i for i, j in k], [j for i, j in k]]
    #downerror = downerrorxy[1]
    plt.xlabel(Xtitle)
    plt.ylabel(Ytitle)
    plt.fill_between(x, uperror2, downerror2, color='skyblue', label='uncertainty2')
    plt.fill_between(x, uperror1, downerror1, color='dodgerblue', label='uncertainty1')
    plt.plot(x, y, colorCurve, label=namePlot)
    plt.legend()


    plt.savefig(untype)
    plt.show()


def plotWith1Bands1Error(namePlot,untype,tupleList,tuplesError1,colorCurve='k',colorError='r',Xtitle='X',Ytitle='Y'):
    if len(tupleList) != len(tuplesError1):
        print('Lengths of lists of data points are not equal')
        exit()
    g = tupleList
    res = [[i for i, j in g], [j for i, j in g]]
    x = res[0]
    y = res[1]
    h = tuplesError1
    error1 = [[i for i, j in h], [j for i, j in h]]
    uperror1 = error1[0]
    downerror1 = error1[1]




    #downerrorxy = [[i for i, j in k], [j for i, j in k]]
    #downerror = downerrorxy[1]
    plt.xlabel(Xtitle)
    plt.ylabel(Ytitle)
    plt.fill_between(x, uperror1, downerror1, color='b', label='uncertainty1')
    plt.plot(x, y, colorCurve, label=namePlot)
    plt.legend()


    plt.savefig('A3part2awitherror.png')
    plt.show()




#plotWithError('Clay','sdf',makeAverageList(r'C:\Users\ap19062\SPA4601\PyCharmProjects\clay-and-mateusz-project\A3.2\Output'),makeAverageUpErrorList(r'C:\Users\ap19062\SPA4601\PyCharmProjects\clay-and-mateusz-project\A3.2\Output'),makeAverageDownErrorList(r'C:\Users\ap19062\SPA4601\PyCharmProjects\clay-and-mateusz-project\A3.2\Output'))

#makeAverageList(r'C:\Users\ap19062\SPA4601\PyCharmProjects\clay-and-mateusz-project\A3.2\Output')

def plotlist(plotname, listT, color = 'k', xaxis = 'x', yaxis = 'y'):
    x = []
    y = []
    for i in listT:
        x.append(i[0])
        y.append(i[1])
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.plot(x,y,color,label=plotname)
    plt.legend()
    plt.savefig('A3part2a.png')
    plt.show()



