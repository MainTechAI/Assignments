import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from itertools import cycle, islice
from scipy.cluster.hierarchy import dendrogram

#%%

plt.figure(figsize=(27.4, 29.0))

#%% 
np.random.seed(0)

n_samples = 1500

X, y = datasets.make_blobs(n_samples=n_samples,
                             cluster_std=[1.0, 2.5, 0.5],
                             random_state=170)
X = StandardScaler().fit_transform(X)

#%%

d_single = AgglomerativeClustering( linkage='single', distance_threshold=0, n_clusters=None)
single = AgglomerativeClustering( linkage='single', n_clusters=3)
d_complete = AgglomerativeClustering( linkage='complete', distance_threshold=0, n_clusters=None)
complete = AgglomerativeClustering( linkage='complete', n_clusters=4)
d_average = AgglomerativeClustering( linkage='average', distance_threshold=0, n_clusters=None)
average = AgglomerativeClustering( linkage='average', n_clusters=4)
d_ward = AgglomerativeClustering( linkage='ward', distance_threshold=0, n_clusters=None)
ward = AgglomerativeClustering( linkage='ward', n_clusters=3)


clustering_algorithms = (
    ('Single Linkage', single, d_single),
    ('Complete Linkage', complete, d_complete),
    ('Group Average', average, d_average),
    ('Ward Linkage', ward, d_ward),
)


#%%

def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)


#%%

plot_num = 1

for name, algorithm, dendro in clustering_algorithms:

    algorithm.fit(X)

    if hasattr(algorithm, 'labels_'):
        y_pred = algorithm.labels_.astype(int)
    else:
        y_pred = algorithm.predict(X)


    plt.subplot(len(clustering_algorithms), 2, plot_num)
    plt.title(name, size=18)
    colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
                                         '#f781bf', '#a65628', '#984ea3',
                                         '#999999', '#e41a1c', '#dede00']),
                                  int(max(y_pred) + 1))))
    plt.scatter(X[:, 0], X[:, 1], s=10, color=colors[y_pred])
    plt.xlim(-2.5, 2.5)
    plt.ylim(-2.5, 2.5)
    plt.xticks(())
    plt.yticks(())
    plot_num += 1

    # dendrogram
    dendro.fit(X)
    plt.subplot(len(clustering_algorithms), 2, plot_num)
    plt.title('Hierarchical Clustering Dendrogram')
    plot_dendrogram(dendro, truncate_mode='level', p=3)
    plt.xlabel("Number of points in node (or index of point if no parenthesis).")
    plot_num += 1



#plt.show()
plt.savefig('10.png')
plt.close()




#%%



#model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)



