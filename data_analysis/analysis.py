"""

- We can add dictionaries and lists to DataFrame
- If need help can type dir(df1)
- df1.<<Column>> is a DataFrame which contains almost same methods than "pandas.DataFrame"

"""
import pandas

data_df1 = []
data_df1.append(["John", 26])
data_df1.append(["Jane", 28])
data_df1.append(["Paul", 45])
data_df1.append(["Nana", 23])
data_df1.append(["Jeff", 35])
data_df1.append(["Alan", 52])

df1 = pandas.DataFrame(data_df1, columns=["Name", "Age"])

data_df2 = []
data_df2.append({"Profession": "Programmer", "Salary": 50000})
data_df2.append({"Profession": "Engineer", "Salary": 70000})
data_df2.append({"Profession": "Lawyer", "Salary": 65000})
data_df2.append({"Profession": "Carpenter", "Salary": 40000})
data_df2.append({"Profession": "Waitress", "Salary": 35000})

df2 = pandas.DataFrame(data_df2, columns=["Profession", "Salary"])

print(df1)
print("\nMean age is %2.2f" % df1.Age.mean())
print("Max age is %2.2f" % df1.Age.max())
print("Min age is %2.2f" % df1.Age.min())
print(df2)
print("\nMean salary is $%2.2f" % df2.Salary.mean())
print("Max salary is $%2.2f" % df2.Salary.max())
print("Min salary is $%2.2f" % df2.Salary.min())

"""
It is possible to load data in many formats
"""
print("\nFrom JSON")
df3 = pandas.read_json("supermarkets.json")
print(df3)

print("\nFrom CSV")
df4 = pandas.read_csv("supermarkets.csv")
print(df4)

print("\nFrom Excel")
df5 = pandas.read_excel("supermarkets.xlsx", sheet_name=0)
print(df5)

print("\nFrom txt comma separated")
df6 = pandas.read_csv("supermarkets-commas.txt")
print(df6)

print("\nFrom txt semi-colons separated")
df7 = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")
print(df7)