import pandas as pd


data = {
    "Product":["Laptop","Phone","Tablet"],
    "Price":[900,500,300],
    "Sales":[50,120,80]

}

df = pd.DataFrame(data)
print(df)