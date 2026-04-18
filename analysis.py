import pandas as pd

data = {
    "Name": ["John", "Mary", "Paul", "Ayo"],
    "Age": [23, 25, 30, 28],
    "Score": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("Full Data:")
print(df)

print("\nAverage Age:", df["Age"].mean())
print("Average Score:", df["Score"].mean())
