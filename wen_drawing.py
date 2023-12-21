import matplotlib.pyplot as plt
import numpy as np
import random as rd

# x = np.linspace(-1,1,50)#从(-1,1)均匀取50个点
# y = 2 * x

# plt.plot(x,y)
# plt.show()

y_data1 = [420, 1760, 8960, 17220]
y_data2 = [a * rd.uniform(1.0, 1.2) for a in y_data1]
y_data3 = [a * rd.uniform(1.0, 1.2) for a in y_data2]

y_data4 = [210, 1980, 6720, 13400]
y_data5 = [a * rd.uniform(1.0, 1.2) for a in y_data1]
y_data6 = [a * rd.uniform(1.0, 1.2) for a in y_data2]

x_data = [7, 11, 16, 21]

# y_data = [0,5000,10000,15000,20000]
# plt.plot(x_data,y_data)
# plt.axis([7,21,0,20000])

# x = [7, 11, 16, 21]
# y = [0, 2000, 4000, 6000, 8000, 10000, 12000, 14000]
# plt.plot(x_data,y_data)
# plt.show()


l1, = plt.plot(x_data, y_data1, label='data1')
l2, = plt.plot(x_data, y_data2, label='data2')
l3, = plt.plot(x_data, y_data3, label='data3')

l4, = plt.plot(x_data, y_data4, label='data1')
l5, = plt.plot(x_data, y_data5, label='data2')
l6, = plt.plot(x_data, y_data6, label='data3')
plt.legend(handles=[l1, l2, l3, l4, l5, l6], labels=['data1', 'data2', 'data3', 'data4', 'data5', 'data6'], loc='best')

plt.xlabel('number of flows')
plt.ylabel('Total delay time')
plt.title('The result of total delay time TTF-based fot different c')
plt.show()
