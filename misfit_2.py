import numpy as np
import pandas as pd
from gpoly import gpoly,plot_model
import matplotlib.pyplot as plt

'''
this code can be used to model 2 polygons, given that you use a minimization function that accepts 2D inputs.
'''

def get_thetas(num=4,):
    thetas = [(i*2*np.pi/num)+(np.pi/4) for i in range(num)]

    return thetas


def squares_2(r,theta,rho=-2.5, plot=False, z_0=1,x_0=.52):
    
    assert len(r) == len(theta), 'inconsistent number of polygons'

    grav_pred=[]
    verts= []
    grav_obs = pd.read_csv('data/tunnel.csv',index_col=0)
    obs = np.array([[i,0] for i in grav_obs.index])
    
    for i in range(len(r)):
        r_i=r[i]
        t_i=theta[i]

        assert len(r_i) == len(t_i), 'r and theta should be the same length'
        verts_i=[]
    
        for j in range(len(r_i)):
            x_i = r_i[j]*np.cos(t_i[j])+x_0
            z_i = r_i[j]*np.sin(t_i[j])+z_0
    
            verts_i.append([x_i,z_i])
        # print(verts_i)
        # print(obs)
        grav_pred_i = gpoly(obs, verts_i, rho) # gravatational potental predicted by forward modeling

        verts.append(verts_i)
        grav_pred.append(grav_pred_i)
    
    grav_pred = np.array(grav_pred)
    grav_pred = grav_pred[0]+grav_pred[1]
    print(grav_pred)
    if plot:
        plot_model(grav_pred,obs,verts[0],verts[1])
        plt.show()
        # plt.scatter(obs,grav_obs['GRAV'].values)
        # plt.scatter(obs,grav_pred)
        # plt.show()

    
    return np.sum(((grav_pred-grav_obs['GRAV'].values))**2)





