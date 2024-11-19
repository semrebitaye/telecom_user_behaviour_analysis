from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd

def calculate_metrics(df):
    df['Total Data (MB)'] = df['DL Data'] + df['UL Data']
    df['Session Duration (Hours)'] = df['Duration'] / 3600
    return df

def kmeans_clustering(df, columns, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(df[columns])
    return df, kmeans

def pca_dimensionality_reduction(df, columns, n_components=2):
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(df[columns])
    return components, pca
