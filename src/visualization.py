import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_matrix(df, columns):
    corr_matrix = df[columns].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

def plot_clusters(df, x_col, y_col, cluster_col):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=cluster_col, palette='viridis')
    plt.title("Cluster Visualization")
    plt.show()
