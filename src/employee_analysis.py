#!/usr/bin/env python
# coding: utf-8

# # Employee Data Analysis
# 
# ## Week 1 - Task 4
# 
# ### Objectives
# 
# - Load employee data
# - Analyze employee salaries
# - Find department-wise employee counts
# - Identify Chennai employees
# - Measure execution time

# In[3]:


import pandas as pd
import numpy as np

# Read employee CSV file
df = pd.read_csv("../data/employees.csv")

# Display employee data
print("Employee Details:")
display(df)

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display column information
print("\nDataset Information:")
df.info()


# In[4]:


import pandas as pd
import numpy as np

# Load employee CSV file
df = pd.read_csv("../data/employees.csv")

# Display employee data
print("Employee Details:")
display(df)

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Dataset information
print("\nDataset Information:")
df.info()

# Statistical description
print("\nStatistical Description:")
display(df.describe())


# In[5]:


# Count employees in each department
department_count = df["department"].value_counts()

print("Department-wise Employee Count:")
print(department_count)


# In[6]:


chennai_employees = df[df["city"] == "Chennai"]

print("Employees from Chennai:")
display(chennai_employees)


# In[7]:


get_ipython().run_line_magic('timeit', 'df["salary"].mean()')


# In[8]:


import pandas as pd
import numpy as np

print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)
print("Libraries imported successfully!")


# In[9]:


# Read employee CSV file
df = pd.read_csv("../data/employees.csv")

# Display employee details
print("Employee Details:")
display(df)

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display dataset information
print("\nDataset Information:")
df.info()

# Display statistical description
print("\nStatistical Description:")
display(df.describe())


# In[10]:


# Count employees in each department
department_count = df["department"].value_counts()

print("Department-wise Employee Count:")
print(department_count)


# In[11]:


# Calculate average salary
average_salary = df["salary"].mean()

# Find highest salary
highest_salary = df["salary"].max()

# Find lowest salary
lowest_salary = df["salary"].min()

print("Salary Analysis:")
print("Average Salary:", round(average_salary, 2))
print("Highest Salary:", highest_salary)
print("Lowest Salary:", lowest_salary)


# In[12]:


get_ipython().run_line_magic('timeit', 'df["salary"].mean()')


# In[ ]:




