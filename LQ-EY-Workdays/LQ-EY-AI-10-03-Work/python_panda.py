import pandas as pd


data = {
    "Product":["Laptop","Phone","Tablet","Broom"],
    "Price":[900,500,300,400],
    "Sales":[50,120,80,200],
    "Status":["Used","New","Used-Good","New"]
}

df = pd.DataFrame(data)
print(df)

cf = pd.read_csv("Student.csv")

print()
print(cf)