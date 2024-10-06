import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#url with data
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'


#load data into df
df = pd.read_csv(url)

missing_data = df.isnull().sum()

age_50plus = df[df['Age'] > 50]

survival_rate_by_gender = df.groupby('Sex')['Survived'].mean()

avg_fare_by_class = df.groupby('Pclass')['Fare'].mean()

# Fill missing values in the 'Age' column with the median age
df['Age'] = df['Age'].fillna(df['Age'].median())

# Verify that no missing values remain in the 'Age' column
#print(df['Age'].isnull().sum())

def categorize_age(age):
    # Check if the input is numeric
    if not isinstance(age, (int, float)):
        return 'Invalid age'  # Return a specific string or handle it as needed

    if age < 18:
        return "Child"
    elif age >= 18 and age <= 60:
        return 'Adult'
    else:
        return 'Senior'

# Apply the categorize_age function to the 'Age' column
df['Age_Group'] = df['Age'].apply(categorize_age)

survival_pivot = df.pivot_table(values='Survived', index='Sex', columns='Pclass', aggfunc='mean')
#print(survival_pivot)

# Group by 'Sex' and calculate the mean survival rate for each gender
survival_by_gender = df.groupby('Sex')['Survived'].mean()




#correlation_matrix = df.corr()

# Display the correlation matrix
#print(correlation_matrix)

# Sample DataFrame (replace this with your actual DataFrame)
data = {
    'Name': ['Braund, Mr. Owen Harris', 'Heikkinen, Miss. Laina', 'Futrelle, Mrs. Jacques Heath'],
    'Age': [22, 26, 35],
    'Fare': [7.25, 7.92, 53.1],
    'Survived': [0, 1, 1]
}
df1 = pd.DataFrame(data)

# Check data types
print(df1.dtypes)

# Select only numeric columns
numeric_df = df1.select_dtypes(include=[np.number])

# Calculate correlation matrix
correlation_matrix = numeric_df.corr()

# Print the correlation matrix
print(correlation_matrix)