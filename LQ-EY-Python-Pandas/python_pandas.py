import pandas as pd

df_Student=pd.read_csv("Student.csv")
df_Sales=pd.read_csv("Sales.csv")

'''

print(df_Student.info())
print(df_Sales.info())

'''

df_Student_Columns=df_Student["Student_Name"]

    # The head() method returns the headers and 
    # a specified number of rows, starting from the top.
        # df.head(*) * being any real integer
        # df.head() prints first 5 rows from the top
df_Student_Head=df_Student.head(3)

    # The tail() method returns the headers and 
    # a specified number of rows, starting from the bottom.
        # df.til(*) * being any real integer
        # df.tail() prints last 5 rows from the bottom

df_Student_Tail=df_Student.tail(3)


    # The info() gives information about the data set
        # It will print the details in a row
            # Name of each column
            # Datat Type of each column
            # The info() method also tells us how many 
            # Non-Null values there are present in each column. 
            # If there are null values in a column, then the 
            # non-null value will be less then the entries value.

df_Student_Info=df_Student.info()


'''
    Outputs/Print Statements
'''

print(df_Student_Info)
