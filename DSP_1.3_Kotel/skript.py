import matplotlib.pyplot as plt

# Импортируем один из пакетов Matplotlib
import pylab


pylab.figure (1)
pylab.subplot (2, 1, 1)
words = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/outFirst1.txt").read().split()
x = [float(v) for k, v in enumerate(words) if k % 2]
y = [float(v) for k, v in enumerate(words) if not k % 2]
#plt.plot(y, x)ax[0][0].plot(y,x , color = 'black')
pylab.plot (y, x, color = 'black')
plt.grid()
plt.title(" Сиглал из выбрки 1,5F")
pylab.subplot (2, 1, 2)
words2 = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/result1.txt").read().split()
x2 = [float(v) for k, v in enumerate(words2) if k % 2]
y2 = [float(v) for k, v in enumerate(words2) if not k % 2]
pylab.plot (y2, x2, 'm' )
plt.title(" Восстановленный сигнал 1,5F")
plt.grid()




pylab.figure (2)
pylab.subplot (2, 1, 1)
#words = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/result1.txt").read().split()
words = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/outFirst2.txt").read().split()

x = [float(v) for k, v in enumerate(words) if k % 2]
y = [float(v) for k, v in enumerate(words) if not k % 2]
#plt.plot(y, x)ax[0][0].plot(y,x , color = 'black')
pylab.plot (y, x, color = 'black')
plt.grid()
plt.title(" Сиглал из выбрки 1,75F")

pylab.subplot (2, 1, 2)
words2 = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/result2.txt").read().split()
x2 = [float(v) for k, v in enumerate(words2) if k % 2]
y2 = [float(v) for k, v in enumerate(words2) if not k % 2]
pylab.plot (y2, x2, 'm' )
plt.title(" Восстановленный сигнал 1,75F")

pylab.grid()



pylab.figure (3)
pylab.subplot (2, 1, 1)
#words = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/result2.txt").read().split()
words = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/outFirst3.txt").read().split()

x = [float(v) for k, v in enumerate(words) if k % 2]
y = [float(v) for k, v in enumerate(words) if not k % 2]
#plt.plot(y, x)ax[0][0].plot(y,x , color = 'black')
pylab.plot (y, x, color = 'black')
plt.grid()
plt.title(" Сиглал из выбрки 2F")

pylab.subplot (2, 1, 2)
words2 = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/result3.txt").read().split()
x2 = [float(v) for k, v in enumerate(words2) if k % 2]
y2 = [float(v) for k, v in enumerate(words2) if not k % 2]

pylab.plot (y2, x2, 'm' )
plt.title(" Восстановленный сигнал 2F")

pylab.grid()


pylab.figure (4)
pylab.subplot (2, 1, 1)
#words = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/result3.txt").read().split()
words = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/outFirst4.txt").read().split()

x = [float(v) for k, v in enumerate(words) if k % 2]
y = [float(v) for k, v in enumerate(words) if not k % 2]
#plt.plot(y, x)ax[0][0].plot(y,x , color = 'black')
pylab.plot (y, x, color = 'black')
plt.grid()
plt.title(" Сиглал из выбрки 3F")

pylab.subplot (2, 1, 2)
words2 = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/result4.txt").read().split()
x2 = [float(v) for k, v in enumerate(words2) if k % 2]
y2 = [float(v) for k, v in enumerate(words2) if not k % 2]
pylab.plot (y2, x2, 'm' )
plt.title(" Восстановленный сигнал 3F")

pylab.grid()



pylab.figure (5)
pylab.subplot (2, 1, 1)
#words = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/result4.txt").read().split()
words = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/outFirst5.txt").read().split()
x = [float(v) for k, v in enumerate(words) if k % 2]
y = [float(v) for k, v in enumerate(words) if not k % 2]
pylab.plot (y, x, color = 'black')
plt.grid()
plt.title(" Сиглал из выбрки 1000F")
pylab.subplot (2, 1, 2)
words2 = open("c:/Users/user/source/repos/DSP_1.3_Kotel/DSP_1.3_Kotel/result5.txt").read().split()
x2 = [float(v) for k, v in enumerate(words2) if k % 2]
y2 = [float(v) for k, v in enumerate(words2) if not k % 2]
pylab.plot (y2, x2, 'm' )
plt.title(" Восстановленный сигнал 1000F")

pylab.grid()

plt.show()
