import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
from sklearn.neighbors import LocalOutlierFactor

# from matrixprofile.org
import matrixprofile as mp
from matrixprofile.visualize import plot_discords_mp
import warnings
warnings.filterwarnings("ignore")

#%%

def nestedLoop(X, r, alpha):
    D_len = X.shape[0]
    y_pred = np.zeros(D_len)
    for i in range(len(X)):
        count = 0
        for j in range(len(X)):
            # Euclidean norm - sqrt(x1^2+x2^2)
            if np.linalg.norm(X[i]) != np.linalg.norm(X[j]) and \
               np.linalg.norm(X[i] - X[j]) <= r:
                count += 1
            if count >= alpha * D_len:
                y_pred[i] = 1
                break         
    return y_pred

#%% dataset1

np.random.seed(0)
rng = np.random.RandomState(42)

n_samples = 300
outliers_fraction = 0.09
n_outliers = int(outliers_fraction * n_samples)
n_inliers = n_samples - n_outliers

X = make_blobs(centers=[[0, 0], [0, 0]], cluster_std=0.5, 
               random_state=0, n_samples=n_inliers, n_features=2)[0]

X = np.concatenate([X, rng.uniform(low=-6, high=6,
                       size=(n_outliers, 2))], axis=0)

#%% plot original dataset1

fig = plt.figure(figsize=(10, 7))
plt.scatter(X[:, 0], X[:, 1], color='orange', edgecolor = 'k')
plt.title('Dataset1 Original')
# plt.show()
plt.savefig('Dataset1.png')
plt.close()

#%% dataset1 clustering

y_pred = DBSCAN(eps=0.5, min_samples=10).fit_predict(X)
fig = plt.figure(figsize=(10, 7))
plt.scatter(X[:, 0], X[:, 1], c=y_pred, edgecolor = 'k')
plt.title('Dataset1. Clustering.')
# plt.show()
plt.savefig('Dataset1 clustering.png')
plt.close()

#%% dataset1 nested loop
        
y_pred = nestedLoop(X, 0.8, 0.03)
        
fig = plt.figure(figsize=(10, 7))        
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap = 'bwr', edgecolor = 'k')
plt.title('Dataset1. Nested loop.')
# plt.show()
plt.savefig('Dataset1 nested loop.png')
plt.close()

#%% dataset2

X = make_blobs(centers=[[2, 2], [-2, -2]], cluster_std=[0.5, 0.5],
               random_state=0, n_samples=n_inliers, n_features=2)[0]

X = np.concatenate([X, rng.uniform(low=-6, high=6,
                       size=(n_outliers, 2))], axis=0)

#%% plot original dataset2

fig = plt.figure(figsize=(10, 7))
plt.scatter(X[:, 0], X[:, 1], color='orange', edgecolor = 'k')
plt.title('Dataset2 Original')
# plt.show()
plt.savefig('Dataset2.png')
plt.close()

#%% dataset2 clustering

y_pred = LocalOutlierFactor(n_neighbors=10).fit_predict(X)

fig = plt.figure(figsize=(10, 7))
plt.scatter(X[:, 0], X[:, 1], c=y_pred, edgecolor = 'k')
plt.title('Dataset2. Clustering.')
# plt.show()
plt.savefig('Dataset2 clustering.png')
plt.close()

#%% dataset2 nested loop

y_pred = nestedLoop(X, 1.0, 0.05)
        
fig = plt.figure(figsize=(10, 7))        
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap = 'bwr', edgecolor = 'k')
plt.title('Dataset2. Nested loop.')
#plt.show()
plt.savefig('Dataset2 nested loop.png')
plt.close()

#%% data

input_file = 'ItalyPowerDemand.txt'
f = open(input_file, 'r')
lines = f.readlines()
dataset = []
for line in lines: 
    dataset.append(float(line))
dataset = np.array(dataset)

#%% discords

window_size = 2*24
k = 2

profile = mp.compute(dataset, window_size)
profile = mp.discover.discords(profile, k = k, exclusion_zone = window_size)
plot_discords_mp(profile)
# plt.show()
plt.savefig('Discords.png')

#%% plot data with highlighted anomalies

fig, ax = plt.subplots(1, 1, sharex=True, figsize=(16,3))
ax.plot(np.arange(len(profile['data']['ts'])), profile['data']['ts'])
ax.set_title('Italian power demand dataset')
ax.set_ylabel('Data')

for i,discord in enumerate(profile['discords']):
    x = np.arange(discord, discord + profile['w'])
    y = profile['data']['ts'][discord:discord + profile['w']]
    ax.plot(x, y, color='red')
    
# plt.show()
plt.savefig('Anomalies.png')
