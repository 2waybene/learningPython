import numpy as np
from numpy import array
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def g(x,y):
  return np.sqrt(x**2-(4*y**2))

'''
def data_for_surface (center_x,center_y,radius,height_z):
    #(x,y):
    z = np.linspace(0, height_z, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    theta_grid, z_grid=np.meshgrid(theta, z)
    x_grid = radius*np.cos(theta_grid) + center_x
    y_grid = radius*np.sin(theta_grid) + center_y
    return x_grid,y_grid,z_grid
'''

def data_for_surface (x,y):
    X=list()
    Y=list()
    Z=list()

    for i in range(len(x)):
        index  =0
        if ((x[i]**2 - 4*y[i]**2) >=0):
            X[index] = x[i]
            #X[index],Y[index],Z[index]=x[i],y[i],g(x[i],y[i])
            index += 1
            print(X[index])
    return X,Y,Z

def plotIt (X,Y,Z):
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.set_title('z = $\sqrt{x^2-4y^2}$')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


#x = np.linspace(-1,1)
x = np.linspace(10,20,1)
y = np.linspace(1,10,1)

A,B,C = data_for_surface(x, y)


print(type(B))
print (len(B))

#print(X.shape)


'''

ax = plt.axes(projection='3d')
#ax.plot_surface(X, Y, Z)
ax.set_title('z = $\sqrt{x^2-4y^2}$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

'''

# plotIt(X,Y,Z)
#for i in range(len(x)):
#    print(x[i])
