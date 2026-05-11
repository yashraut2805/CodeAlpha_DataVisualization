import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset/StudentsPerformance.csv")

# Show first 5 rows
print(df.head())

# Dataset info
print(df.info())

# Average scores
average_scores = df[['math score', 'reading score', 'writing score']].mean()

# Bar chart for average scores
plt.figure(figsize=(6,5))
average_scores.plot(kind='bar')
plt.title("Average Scores of Students")
plt.ylabel("Scores")
plt.show()

# Gender distribution
plt.figure(figsize=(5,5))
df['gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# Parental education impact
plt.figure(figsize=(10,5))
sns.boxplot(x='parental level of education', y='math score', data=df)
plt.xticks(rotation=20)
plt.title("Parental Education vs Math Score")
plt.show()

# Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df[['math score', 'reading score', 'writing score']].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()