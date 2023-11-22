import numpy as np
import pandas as pd
from gpoly import gpoly,plot_model
import matplotlib.pyplot as plt

def get_thetas(num=4):
    thetas = [(i*2*np.pi/num)+(np.pi/4) for i in range(num)]

    return thetas


def dist(r,theta,rho=-2.5, plot=False):

    assert len(r) == len(theta), 'r and theta should be the same length'

    verts=[]

    for i in range(len(r)):
        x_i = r[i]*np.cos(theta[i])
        z_i = r[i]*np.sin(theta[i])+1

        verts.append([x_i,z_i])

    grav_obs = pd.read_csv('data/tunnel.csv',index_col=0)


    obs = np.array([[i,0] for i in grav_obs.index])

    grav_pred = gpoly(obs, verts, rho) # gravatational potental predicted by forward modeling

    if plot:
        plot_model(grav_pred,obs,verts)

    
    return np.sum(((grav_pred-grav_obs['GRAV'].values)/grav_obs['GRAV'].values)**2)





