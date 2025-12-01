import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('seaborn_exercise/Titanic-Dataset.csv')
# print(df)

# compute numeric correlation
corr = df.corr(numeric_only=True)
print(corr)

# 1. correlation heatmap
plt.figure(figsize=(10,8))
plt.imshow(corr, aspect='auto')
plt.xticks(range(len(corr.columns)), corr.columns, rotation= 90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.colorbar()
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig("titanic_data_correlation/correlation.png", dpi=300, bbox_inches="tight")

# plt.show()

# 2. Age Distribution Histogram 
plt.figure(figsize=(8,5))
plt.hist(df['Age'].dropna())
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age Distribution')
plt.tight_layout()
plt.savefig("titanic_data_correlation/Age Distribution.png", dpi=300, bbox_inches="tight")

# plt.show()

# 4. Survived Count Bar Chart
plt.figure(figsize=(6, 5))
df['Survived'].value_counts().plot(kind='bar')
plt.xlabel("Survived")
plt.ylabel("Count")
plt.title("Survival Count")
plt.tight_layout()
plt.savefig("titanic_data_correlation/Survived.png", dpi=300, bbox_inches="tight")

# plt.show()

# 5. Passenger Class Distribution
plt.figure(figsize=(6, 5))
df['Pclass'].value_counts().plot(kind='bar')
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.title("Passenger Class Distribution")
plt.tight_layout()
plt.savefig("titanic_data_correlation/Passenger.png", dpi=300, bbox_inches="tight")

# plt.show()



# 6. Age vs Fare Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['Fare'])
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare")
plt.tight_layout()
plt.savefig("titanic_data_correlation/Age vs Fare.png", dpi=300, bbox_inches="tight")

# plt.show()


# 7. SibSp vs Parch Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(df['SibSp'], df['Parch'])
plt.xlabel("Siblings/Spouses Aboard")
plt.ylabel("Parents/Children Aboard")
plt.title("SibSp vs Parch")
plt.tight_layout()
plt.savefig("titanic_data_correlation/SibSp vs Parch.png", dpi=300, bbox_inches="tight")

# plt.show()


# 8. Survival Rate by Passenger Class
plt.figure(figsize=(8, 5))
df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.title("Survival Rate by Class")
plt.tight_layout()
plt.savefig("titanic_data_correlation/Survival Rate by Passenger Class.png", dpi=300, bbox_inches="tight")

# plt.show()


plt.show()