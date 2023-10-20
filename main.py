import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("adult.csv")

plt.figure(figsize=(14,6))

plt.title("Some Adult Shit Data...")

sns.lineplot(data=df['salary'])

plt.show()