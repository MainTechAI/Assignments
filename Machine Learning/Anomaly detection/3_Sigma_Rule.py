import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

np.random.seed(0)

#%% dataset1

X1 = np.random.uniform(0.4, 0.6,100)
abnormal = np.random.uniform(0.1, 0.4,5)
X1=np.append(X1,abnormal)
abnormal = np.random.uniform(0.6, 1.0,5)
X1=np.append(X1,abnormal)

#%% Dataset1 histogram

percent = 0.24
num_bins = 30

fig = plt.figure(figsize=(10, 5))
count, bins, ignored = plt.hist(X1, num_bins, density=True, edgecolor='k')
plt.title('Dataset 1', fontsize=15)
plt.xlabel('x')
plt.ylabel('frequency')
plt.xlim(0.0, 1.1)  


# dots
density1, bins1 = np.histogram(X1, density=True, bins=num_bins)

threshold1 = max(density1) * percent

normal = []
anomaly = []
for x in X1:
    for i in range(0, len(bins1)-1):
        if( bins1[i] <= x and x <= bins1[i+1] ):
            if(density1[i] > threshold1):
                normal.append(x)
            else:
                anomaly.append(x)


plt.plot(normal, np.zeros_like(normal)-0.1,'o', alpha=0.6, color='green', label='normal')
plt.plot(anomaly, np.zeros_like(anomaly)-0.1,'o', alpha=0.6, color='red', label='anomaly')
plt.plot(np.linspace(0.0,1.0,100), np.zeros(100)+threshold1, '--', color='red')
plt.legend()
plt.show()
#plt.savefig('dataset1_histogram.png')
plt.close()


#%% Dataset1 3 sigma

sigma = np.std(X1)
mu = np.mean(X1)
k = 2
print('sigma = ',sigma)
print('mu = ',mu)
normal = []
anomaly = []

for i in range(0, len(X1)):
    if( (mu-k*sigma) <= X1[i] <=  (mu+k*sigma) ):
        normal.append(X1[i])
    else:
        anomaly.append(X1[i])
        
      

fig = plt.figure(figsize=(10, 5))
count, bins, ignored = plt.hist(X1, num_bins, density=True, edgecolor='k')
plt.title('Dataset 1. 3 sigma', fontsize=15)
plt.xlabel('x')
plt.ylabel('frequency')
plt.xlim(0.0, 1.1)  
  
      
plt.plot(normal, np.zeros_like(normal)-0.1,'o', alpha=0.6, color='green', label='normal')
plt.plot(anomaly, np.zeros_like(anomaly)-0.1,'o', alpha=0.6, color='red', label='anomaly')
#plt.plot(np.linspace(0.0,1.0,100), np.zeros(100)+threshold1, '--', color='red')
plt.legend()
plt.show()
#plt.savefig('dataset1_histogram.png')
plt.close()    

#%% dataset2

X2 = np.random.uniform(0.3, 0.6,100)
anomaly1 = np.random.uniform(0.01, 0.2,5)
anomaly2 = np.random.uniform(0.7, 0.99,8)
X2=np.append(X2,anomaly1)
X2=np.append(X2,anomaly2)

# histogram
percent = 0.24
num_bins = 30


fig = plt.figure(figsize=(10, 5))
count, bins, ignored = plt.hist(X2, num_bins, density=True, edgecolor='k')
plt.title('Dataset 2', fontsize=15)
plt.xlabel('x')
plt.ylabel('frequency')
plt.xlim(0.0, 1.1)  


# dots
density2, bins2 = np.histogram(X2, density=True, bins=num_bins)

threshold2 = max(density2) * percent

normal = []
anomaly = []
for x in X2:
    for i in range(0, len(bins2)-1):
        if( bins2[i] <= x and x <= bins2[i+1] ):
            if(density2[i] > threshold2):
                normal.append(x)
            else:
                anomaly.append(x)


plt.plot(normal, np.zeros_like(normal)-0.1,'o', alpha=0.6, color='green', label='normal')
plt.plot(anomaly, np.zeros_like(anomaly)-0.1,'o', alpha=0.6, color='red', label='anomaly')
plt.plot(np.linspace(0.0,1.0,100), np.zeros(100)+threshold2, '--', color='red')
plt.legend()
plt.show()
#plt.savefig('dataset2_histogram.png')
plt.close()


#%% Dataset2 3 sigma

sigma = np.std(X2)
mu = np.mean(X2)
k = 2

print('sigma = ',sigma)
print('mu = ',mu)

normal = []
anomaly = []

for i in range(0, len(X2)):
    if( (mu-k*sigma) <= X2[i] <=  (mu+k*sigma) ):
        normal.append(X2[i])
    else:
        anomaly.append(X2[i])
        
      

fig = plt.figure(figsize=(10, 5))
count, bins, ignored = plt.hist(X2, num_bins, density=True, edgecolor='k')
plt.title('Dataset 2. 3 sigma', fontsize=15)
plt.xlabel('x')
plt.ylabel('frequency')
plt.xlim(0.0, 1.1)  
  
      
plt.plot(normal, np.zeros_like(normal)-0.1,'o', alpha=0.6, color='green', label='normal')
plt.plot(anomaly, np.zeros_like(anomaly)-0.1,'o', alpha=0.6, color='red', label='anomaly')
#plt.plot(np.linspace(0.0,1.0,100), np.zeros(100)+threshold1, '--', color='red')
plt.legend()
plt.show()
#plt.savefig('dataset1_histogram.png')
plt.close()    
