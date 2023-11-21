import numpy as np
import pandas as pd
from gpoly import gpoly

def get_thetas(num=4):
    thetas = [i*360/4 for i in range(num)]

    return thetas


def dist(r,theta,rho=2.5):

    assert len(r) == len(theta[i]), 'r and theta should be the same length'

    verts=[]

    for i in range(len(r)):
        x_i = r[i]*np.cos(theta[i])
        z_i = r[i]*np.sin(theta[i])

        verts.append([x_i,z_i])

    grav_obs = pd.read_csv('data/tunnel.csv')


    obs = grav_obs.index

    grav_pred = gpoly(obs, verts, rho) # gravatational potental predicted by forward modeling

    return np.sum(((grav_pred-grav_obs)/grav_obs)**2)



