import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_circles, make_blobs

#%% 1

rs = 170
n_samples = 1500

X, _ = make_circles(n_samples=n_samples, factor=.5, noise=.05)
X = StandardScaler().fit_transform(X)

min_samples = list(range(3,10))
# min_samples.append(70)
eps = [0.2, 0.5, 0.8]

i=1
for ms in min_samples:
    for e in eps:
        y_pred = DBSCAN(eps=e, min_samples=ms).fit_predict(X)
        plt.subplot(len(min_samples), len(eps), i)
        plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='rainbow')
        plt.title('eps:'+str(e)+', min_samples:'+str(ms))
        i+=1
    
    
fig = plt.gcf()
fig.set_size_inches(28,28)
plt.savefig('9.1.png')
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

min_samples = list(range(3,10))
# min_samples.append(70)
eps = [0.2, 0.5, 0.8]

X, _ = make_blobs(n_samples=n_samples, random_state=rs, centers=4)
X = StandardScaler().fit_transform(X)
noisyX = add_noise(X.copy(), 10, 1.5)


i=1
for ms in min_samples:
    for e in eps:
        y_pred = DBSCAN(eps=e, min_samples=ms).fit_predict(noisyX)
        plt.subplot(len(min_samples), len(eps), i)
        plt.scatter(noisyX[:,0], noisyX[:,1], c=y_pred, cmap='tab10')
        plt.title('eps:'+str(e)+', min_samples:'+str(ms))
        i+=1
        
fig = plt.gcf()
fig.set_size_inches(15,30)
plt.savefig('9.2 noise=10%.png')
plt.close()
    

