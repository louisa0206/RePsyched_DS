import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns;
from sklearn.cluster import KMeans

sns.set()

df = pd.read_csv('location.csv')
# df.head(10)

df.dropna(axis=0, how='any', subset=['latitude', 'longitude'], inplace=True)

# Variable with the Longitude and Latitude
X = df.loc[:, ['id', 'latitude', 'longitude']]
# X.head(10)

K_clusters = range(1, 10)
kmeans = [KMeans(n_clusters=i) for i in K_clusters]
Y_axis = df[['latitude']]
X_axis = df[['longitude']]
score = [kmeans[i].fit(Y_axis).score(Y_axis) for i in range(len(kmeans))]
# Visualize
plt.plot(K_clusters, score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()

kmeans = KMeans(n_clusters=12, init='k-means++')
kmeans.fit(X[X.columns[1:3]])  # Compute k-means clustering.
X['cluster_label'] = kmeans.fit_predict(X[X.columns[1:3]])
centers = kmeans.cluster_centers_  # Coordinates of cluster centers.
labels = kmeans.predict(X[X.columns[1:3]])  # Labels of each point
print(X.head(10))

X.plot.scatter(x='latitude', y='longitude', c=labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()