import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('seaborn_exercise/Titanic-Dataset.csv')
#-----------------------------------------------
# -------------------HeatMap-----------------------
# sns.heatmap(df.select_dtypes(include='number'))
# plt.show()
# corr = df.corr(numeric_only=True)
# sns.heatmap(corr, annot=True, cmap='coolwarm')


# --------------------PairPlot-------------------------
# sns.pairplot(df.select_dtypes(include='number'))
# plt.savefig("pairplot.png", dpi=300, bbox_inches="tight")
sns.pairplot(
    df,
    vars=['Age', 'Fare', 'SibSp', 'Parch'],   # numeric columns
    hue='Survived'
)
# plt.savefig("seaborn_exercise/pairplot.png", dpi=300, bbox_inches="tight")

plt.show()
