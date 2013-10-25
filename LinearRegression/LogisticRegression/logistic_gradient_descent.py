import math
import numpy as np
import matplotlib.pyplot as plt

filex = open('q1x.dat', 'r')
filey = open('q1y.dat', 'r')

dataset_x = []
for line in filex:
    datasource = ['1.0']
    datasource[1:] = line.strip().split('  ')
    dataset_x.append([float(s.strip()) for s in datasource])
filex.close()

dataset_y = []
for line in filey:
    dataset_y.append(float(line.strip()))
filey.close()

print dataset_x
print dataset_y

m = len(dataset_y)

theta0 = np.mat([1,0,0])
theta = np.mat([0, 0, 0])
alpha = 0.01
epsilon = 0.000000001
while True:
    s = 0
    for i in range(len(dataset_y)):
        s += (dataset_y[i] - 1.0 / (1 + math.exp(-1 * np.inner(dataset_x[i], theta)))) * np.mat(dataset_x[i])
    theta = theta + alpha * s
    if np.inner(theta - theta0, theta - theta0) < epsilon:
        break
    else:
        theta0 = theta
    
theta = theta.tolist()[0]
print theta

plt.figure()

posX = []
posY = []

negX = []
negY = []

i = 0
for y in dataset_y:
    if y > 0:
        posX.append(dataset_x[i][1])
        posY.append(dataset_x[i][2])
    else:
        negX.append(dataset_x[i][1])
        negY.append(dataset_x[i][2])
    i = i + 1

originX = np.array(posX)
x1min = min(originX)
x1max = max(originX)
originY = np.array(posY)
plt.plot(originX, originY, 'go')

originX = np.array(negX)
x1min = min(originX)
x1max = max(originX)
originY = np.array(negY)
plt.plot(originX, originY, 'rx')

#theta = [-2.6205, 0.7604, 1.1719]

x = np.arange(x1min, x1max, 0.01)
y = -1 * theta[0]/theta[2] - theta[1]/theta[2]*x
plt.plot(x, y, 'b-')

plt.savefig('figure.png')








