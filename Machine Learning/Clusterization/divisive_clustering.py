import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs,make_circles

#%% 1

rs = 170
n_samples = 1500
n_clusters = list(range(3,10))

X, _ = make_blobs(n_samples=n_samples, random_state=rs, centers=4)
X = StandardScaler().fit_transform(X)

for i, n in enumerate(n_clusters):
    y_pred = KMeans(n_clusters=n, random_state=rs).fit_predict(X)
    plt.subplot(420+i+1)
    # ,alpha=0.5, edgecolor='k'
    plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='tab10')
    plt.title(str(n)+' clusters')
    
    
fig = plt.gcf()
fig.set_size_inches(18,18)
plt.savefig('7.1.png')
plt.close()

#%% 2

def add_noise(data, rate, lvl):
    np.random.shuffle(data)
    n_samples = int(data.shape[0]*rate / 100.0)
    
    for i in range(0, n_samples):        
        state = np.random.randint(low=1, high=8, size=(1,))[0]
        
        if(state==1):
            data[i][0]+= np.random.rand(1)[0]*lvl
        elif(state==2):
            data[i][0]-= np.random.rand(1)[0]*lvl
        elif(state==3):
            data[i][1]+= np.random.rand(1)[0]*lvl
        elif(state==4):  
            data[i][1]-= np.random.rand(1)[0]*lvl
        elif(state==5):    
            data[i][0]+= np.random.rand(1)[0]*lvl
            data[i][1]+= np.random.rand(1)[0]*lvl
        elif(state==6): 
            data[i][0]-= np.random.rand(1)[0]*lvl
            data[i][1]-= np.random.rand(1)[0]*lvl  
        elif(state==6):
            data[i][0]+= np.random.rand(1)[0]*lvl
            data[i][1]-= np.random.rand(1)[0]*lvl
        elif(state==7):
            data[i][0]-= np.random.rand(1)[0]*lvl
            data[i][1]+= np.random.rand(1)[0]*lvl
            
    return data

#%% 2

noise_list = [1, 3, 5, 10]

for noise in noise_list:
    noisyX = add_noise(X.copy(), 10, 1.5)
    i=1
    
    for n in n_clusters:
        y_pred = KMeans(n_clusters=n, random_state=rs).fit_predict(noisyX)
        plt.subplot(7,2,i)
        plt.scatter(noisyX[:,0], noisyX[:,1], c=y_pred, cmap='tab10')
        plt.title(str(n)+' clusters (k‑Means)')
        i+=1
        
        y_pred = KMedoids(n_clusters=n, random_state=rs).fit_predict(noisyX)
        plt.subplot(7,2,i)
        plt.scatter(noisyX[:,0], noisyX[:,1], c=y_pred, cmap='tab10')
        plt.title(str(n)+' clusters (k‑Medoids)')
        i+=1
        
    fig = plt.gcf()
    fig.set_size_inches(15,30)
    plt.savefig('7.2 noise='+str(noise) +'%.png')
    plt.close()
    
    

#%% 3

nonConvex, _ = make_circles(n_samples=n_samples, factor=.5, noise=.05)
i=1
n_clusters = list(range(2,9))

for n in n_clusters:
    y_pred = KMeans(n_clusters=n, random_state=rs).fit_predict(nonConvex)
    plt.subplot(7,2,i)
    plt.scatter(nonConvex[:,0], nonConvex[:,1], c=y_pred, cmap='tab10')
    plt.title(str(n)+' clusters (k‑Means)')
    i+=1
    
    y_pred = KMedoids(n_clusters=n, random_state=rs).fit_predict(nonConvex)
    plt.subplot(7,2,i)
    plt.scatter(nonConvex[:,0], nonConvex[:,1], c=y_pred, cmap='tab10')
    plt.title(str(n)+' clusters (k‑Medoids)')
    i+=1
    
fig = plt.gcf()
fig.set_size_inches(15,30)
plt.savefig('7.3.png')
plt.close()

