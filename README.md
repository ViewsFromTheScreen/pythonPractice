Titanic Data Analysis
This script performs exploratory data analysis on the Titanic dataset. The code loads data, processes missing values, categorizes age groups, calculates survival rates, and visualizes correlations among numerical data.

Dataset
The script uses the Titanic dataset available at the following URL:

ruby
Copy code
https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
This dataset includes information about passengers on the Titanic, such as their age, gender, ticket class, fare, and whether they survived the disaster.

Libraries
The following Python libraries are required to run the script:

pandas: For data manipulation and analysis.
matplotlib.pyplot: For plotting (imported but not used in this script).
numpy: For numerical operations.
Code Overview
Load Data

The data is loaded from a public URL into a Pandas DataFrame (df).

python
Copy code
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
Data Exploration and Cleaning

Missing Data: Calculates the number of missing values in each column.

python
Copy code
missing_data = df.isnull().sum()
Subset of Age > 50: Creates a subset of passengers over 50 years old.

python
Copy code
age_50plus = df[df['Age'] > 50]
Survival Rate by Gender: Calculates the average survival rate for each gender.

python
Copy code
survival_rate_by_gender = df.groupby('Sex')['Survived'].mean()
Average Fare by Passenger Class: Calculates the average fare paid by passengers in each class.

python
Copy code
avg_fare_by_class = df.groupby('Pclass')['Fare'].mean()
Handling Missing Values

Fills missing values in the 'Age' column with the median age to ensure no missing values remain.

python
Copy code
df['Age'] = df['Age'].fillna(df['Age'].median())
Age Group Categorization

Defines a function to categorize passengers by age into three groups: "Child," "Adult," and "Senior."

python
Copy code
def categorize_age(age):
    if not isinstance(age, (int, float)):
        return 'Invalid age'
    if age < 18:
        return "Child"
    elif age >= 18 and age <= 60:
        return 'Adult'
    else:
        return 'Senior'

df['Age_Group'] = df['Age'].apply(categorize_age)
Survival Rate Analysis by Gender and Class

Creates a pivot table to view the mean survival rate by gender and class.

python
Copy code
survival_pivot = df.pivot_table(values='Survived', index='Sex', columns='Pclass', aggfunc='mean')
Correlation Analysis

Analyzes the correlation between numeric variables (such as Age, Fare, and Survived) to identify relationships in the data.

python
Copy code
numeric_df = df1.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()
print(correlation_matrix)
Example Output
The script includes print statements to display:

The data types of selected columns.
The correlation matrix for numerical columns.
Usage
Ensure all necessary libraries are installed.
Run the script in a Python environment to see outputs for missing values, survival rates, and the correlation matrix.
