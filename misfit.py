import numpy as np
import pandas as pd
from gpoly import gpoly,plot_model
import matplotlib.pyplot as plt



def get_thetas(num=4,):
    '''
    get num# evenly spaced angles 

    note: shapes created with these angles will always have an axis of symetry
    ----
    num: int
    the number of verticies in your shape
    '''
    thetas = [(i*2*np.pi/num)+(np.pi/4) for i in range(num)]

    return thetas


def squares(r,theta,rho=-2.5, plot=False, z_0=1,x_0=.52):
    '''
    returns the total distance from the predicted values to the observed values.
    used as part of the least squares algorithm

    the function takes polar co-ordinants for each point because scipy.optimize.minimize can only work with  single dimenssional inputs.
    ---
    r: array, list
    an array contaning the radii asscociated with each angle; listed clock-wise
    
    theta: array,list
    an array containing the angles associated with each radius; listed clock-wise

    rho: int
    the density of the anomaly; g/cc

    plot: bool
    weather or not to plot the model

    z_0: int
    the center of the polygon (z co-ordinate); z positive down

    x_0: int
    the center of the polygon (x co-ordinate)
    '''

    assert len(r) == len(theta), 'r and theta should be the same length'

    verts=[]

    for i in range(len(r)):
        x_i = r[i]*np.cos(theta[i])+x_0
        z_i = r[i]*np.sin(theta[i])+z_0

        verts.append([x_i,z_i])

    grav_obs = pd.read_csv('data/tunnel.csv',index_col=0)


    obs = np.array([[i,0] for i in grav_obs.index])

    grav_pred = gpoly(obs, verts, rho) # gravatational potental predicted by forward modeling

    if plot:
        plot_model(grav_pred,obs,verts)
        plt.show()
        # plt.scatter(obs,grav_obs['GRAV'].values)
        # plt.scatter(obs,grav_pred)
        # plt.show()

    
    return np.sum(((grav_pred-grav_obs['GRAV'].values))**2)





