"""

- We can add dictionaries and lists to DataFrame
- If need help can type dir(df1)
- df1.<<Column>> is a DataFrame which contains almost same methods than "pandas.DataFrame"

"""
import pandas

data_df1 = []
data_df1.append(["COD01", "John", 26, ""])
data_df1.append(["COD02", "Jane", 28, ""])
data_df1.append(["COD03", "Paul", 45, ""])
data_df1.append(["COD04", "Nana", 23, ""])
data_df1.append(["COD05", "Jeff", 35, ""])
data_df1.append(["COD06", "Alan", 52, ""])

df1 = pandas.DataFrame(data_df1, columns=["ID", "Name", "Age", "Category"])

"""

It is possible to define if conditions to generate column values

"""
df1.loc[df1.Age >= 30, "Category"] = "Mature"
df1.loc[df1.Age < 30, "Category"] = "Young"
df1.loc[df1.Age >= 50, "Category"] = "Old"

"""
Se column index to be da column 'ID'
"""
df1 = df1.set_index("ID")

"""

I can also create ranges for unique indexes.
In this case, from ID COD02 to COD04. 
Bringing only from field 'Age' to 'Category'

"""
df1 = df1.loc["COD02":"COD04","Age":"Category"]

"""
And restrict for attributes. In this case, where Age < 45
"""
df1 = df1.loc[df1.Age < 45]

data_df2 = []
data_df2.append({"Profession": "Programmer", "Salary": 50000})
data_df2.append({"Profession": "Engineer", "Salary": 70000})
data_df2.append({"Profession": "Lawyer", "Salary": 65000})
data_df2.append({"Profession": "Carpenter", "Salary": 40000})
data_df2.append({"Profession": "Waitress", "Salary": 35000})

df2 = pandas.DataFrame(data_df2, columns=["Profession", "Salary"])

"""
It is possible to filter results. I.e: Get salaries > 40000
"""
df2 = df2[df2.Salary > 40000]

"""
It is also possible to get objects by specific position index and 
"""
df1_index = pandas.DataFrame(data_df1, columns=["ID", "Name", "Age", "Category"])
df1_index = df1_index.iloc[3, 1:3]
print(df1_index)

"""

And get values from specific index positions and fields

"""
df1_index_value = pandas.DataFrame(data_df1, columns=["ID", "Name", "Age", "Category"])
df1_index_value = df1_index_value.loc[3, "Name"]
print(df1_index_value)

print(df1)
print("\nMean age is %2.2f" % df1.Age.mean())
print("Max age is %2.2f" % df1.Age.max())
print("Min age is %2.2f" % df1.Age.min())
print(df2)
print("\nMean salary is $%2.2f" % df2.Salary.mean())
print("Max salary is $%2.2f" % df2.Salary.max())
print("Min salary is $%2.2f" % df2.Salary.min())

"""

It is possible to drop columns by name

"""
df1_2 = pandas.DataFrame(data_df1, columns=["ID", "Name", "Age", "Category"])
df1_2.drop("Category",1)

"""

It is possible to drop rows by index

"""
df1_3 = pandas.DataFrame(data_df1, columns=["ID", "Name", "Age", "Category"])
df1_3 = df1_3.set_index("ID")
df1_3.drop("COD01",0)

"""

It is possible to drop rows by index positions ranges

"""
df1_4 = pandas.DataFrame(data_df1, columns=["ID", "Name", "Age", "Category"])
df1_4 = df1_4.set_index("ID")
df1_4.drop(df1_4.index[0:3],0)

"""

It is possible to drop columns by index positions ranges

"""
df1_5 = pandas.DataFrame(data_df1, columns=["ID", "Name", "Age", "Category"])
df1_5.drop(df1_5.columns[2:4],1)

"""
It is possible to load data in many formats
"""
df3 = pandas.read_json("supermarkets.json")
df4 = pandas.read_csv("supermarkets.csv")
df5 = pandas.read_excel("supermarkets.xlsx", sheet_name=0)
df6 = pandas.read_csv("supermarkets-commas.txt")
df7 = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")

"""

Add new column 'Continent' for the DataFrame with default value 'North America'

"""
df5_total_columns = df5.shape[0]
df5["Continent"] = df5_total_columns*["North America"]

"""

Update column value for each row

"""
df5["Continent"] = df5["Country"] + ", " + df5["Continent"]

"""

Add a new row for DataFrame

"""
"""
Add a new row for DataFrame
"""
new_id = 7
df5 = df5.set_index("ID")
df5_t = df5.T
df5_t[new_id] = ["Center", "Florianopolis", "Santa Catarian", "Brazil", "Bistek", 700]
df5 = df5_t.T