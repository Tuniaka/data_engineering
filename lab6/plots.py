import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_types(filename):
    with open(filename) as file:
        dtypes = json.load(file)
    for key in dtypes.keys():
        if dtypes[key] == 'category':
            dtypes[key] = pd.CategoricalDtype
        else:
            dtypes[key] = np.dtype(dtypes[key])
    return dtypes

def linear_plot(df, x, y, title, filename):
    plt.title(title)
    sns.lineplot(data=df, x=x, y=y)
    plt.savefig(filename)
    plt.close()

def scatter_plot(df, x, y, title, filename):
    plt.title(title)
    sns.scatterplot(data=df, x=x, y=y)
    plt.savefig(filename)
    plt.close()

def bar_plot(df, x, y, title, filename):
    plt.title(title)
    sns.barplot(data=df, x=x, y=y,)
    plt.savefig(filename)
    plt.close()

def plot_step(data, x, y, title, filename):
	plt.title(title)
	sns.stripplot(data=data.sample(1000), x=x, y=y, dodge=True)
	plt.savefig(filename)
	plt.close()

def plot_histogram(df, x, y, title, filename):
    plt.title(title)
    sns.histplot(data=df.sample(1000), x=x, y=y)
    plt.savefig(filename)
    plt.close()