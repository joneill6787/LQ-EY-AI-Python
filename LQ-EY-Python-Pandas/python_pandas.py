import pandas as pd
from typing import Literal

df_Student=pd.read_csv("./Raw_Data/Student.csv")
df_Sales=pd.read_csv("./Raw_Data/Sales.csv")
df_8bDCE_sheets=pd.read_excel("./Raw_Data/8bData_Cleansing_Exercise.xlsx",sheet_name=[
                                                    'Data Cleansing Exercise',
                                                    'Customer Details'])

s1_8bDCE = df_8bDCE_sheets['Data Cleansing Exercise']
s2_8bDCE = df_8bDCE_sheets['Customer Details']


# Generic Definitions/Variables

exportAllToFile = False

# Data Cleansing

    # == Sheet_1 Cleansing 'Data Cleansing Exercise' ==

        # Format Order Date column

s1_8bDCE['Order Date'] = pd.to_datetime(s1_8bDCE['Order Date'], format='%d.%m.%Y')

        # Format number column

s1_8bDCE['Sales Revenue'] = pd.to_numeric(s1_8bDCE['Sales Revenue']
                                          .str.replace('$','',regex=False),
                                          errors='coerce'
                                          )


    # == Sheet_2 Cleansing 'Customer Details' ==

    # Split Zipcode/State into seperate columns and clean code
s2_8bDCE[['Zipcode','State']] = s2_8bDCE['ZipCode/State'].str.split('/',expand=True)
s2_8bDCE['Zipcode']=pd.to_numeric(s2_8bDCE['Zipcode'],errors='coerce')

        # Drop 'ZipCode/State' as no longer needed
s2_8bDCE = s2_8bDCE.drop(columns='ZipCode/State')

    # Split Customer Name into Cust_FName and Cust_LName
s2_8bDCE[['Cust_FName','Cust_LName']] = s2_8bDCE['Customer Name'].str.split(' ',n=1,expand=True)

        # Drop 'Customer Name' as no longer needed

s2_8bDCE = s2_8bDCE.drop(columns='Customer Name')

    # Reorder Columns

s2_8bDCE = s2_8bDCE[[
    'Customer ID',
    'Cust_FName',
    'Cust_LName',
    'City',
    'State',
    'Zipcode']]



#s2_8bDCE.info()

def findTopLow5Sheet1():
    # Print Highest 5 and Lowest 5

    top5_CID_SR=s1_8bDCE.groupby('Customer ID')['Sales Revenue'].sum().nlargest(5)
    low5_CID_SR=s1_8bDCE.groupby('Customer ID')['Sales Revenue'].sum().nsmallest(5)
    print(top5_CID_SR)
    print(low5_CID_SR)

# s2_8bDCE = s2_8bDCE.drop_duplicates(subset='Customer ID',keep='first')

def sheet2_Dup_Check(df: pd.DataFrame,column_name: str, keep_arg: Literal['first','last',False] = 'first'):

    df = df.drop_duplicates(subset=column_name,keep=keep_arg)
    print(f"Duplicates removed based on column: {column_name}")
    
    return df

def claude_Sheet2_Dup_UniqueCheck():

    cols_to_check = ['Cust_FName', 'Cust_LName', 'State', 'Zipcode']

    inconsistent = s2_8bDCE.groupby('Customer ID')[cols_to_check].nunique()

    # Show only CustomerIDs where ANY of those columns has more than 1 unique value


    print(inconsistent[inconsistent.gt(1).any(axis=1)])
    
    if exportAllToFile:
            # Prints output to CSV if TRUE
        inconsistent[inconsistent.gt(1).any(axis=1)].to_csv('incon_customers.csv')



def groupByChecks():

        # The following code merges the two sheets together
            # If I want to use a column I need to add it to the following section:
            #       s2_8bDCE[['Insert Column Name','Insert Column Name']]
    gbmergeCID = s1_8bDCE.merge(s2_8bDCE[['Customer ID', 'Cust_FName','Cust_LName','State']],
                                left_on='Customer ID',
                                right_on='Customer ID',
                                how='left'
                                )
    
        # The following code prints out the sum of all orders grouped by Customer ID
    
    revByCust= gbmergeCID.groupby(['Customer ID','Cust_FName','Cust_LName'])['Sales Revenue'].sum().reset_index()


        # Adding .head(5) allows me to print only the top 5 results 
            # Adding .to_string(index=False) the index numbers of each row will not be printed out
    print(revByCust.sort_values('Sales Revenue',ascending=False).head(5).to_string(index=False))

    revByState = gbmergeCID.groupby(['State'])['Sales Revenue'].sum().reset_index()
    revByState_Sort = revByState.sort_values('Sales Revenue',ascending=False).head(5).reset_index(drop=True)
    revByState_Sort.index += 1
    revByState_Sort = revByState_Sort.reset_index().rename(columns={'index':'Rank'}).to_string(index=False)


    print(revByState_Sort)


def practiceGroupBy():
    # A little bit of messy code to practice groupby

        # To call all rows in the merged table, simply just call the table

    gbmergeMessy = s1_8bDCE.merge(s2_8bDCE,
                                  left_on='Customer ID',
                                  right_on='Customer ID')
    

    revByCustMess = gbmergeMessy.groupby('Customer ID')['Sales Revenue'].sum().reset_index()

        # Interesting to note, if .reset_index() is not added to the above line, then the below
        # line will not work correctly and merge will not work. It is treated as an 'Object'
            # Correction, without .reset_index() is treated as a 'Series'

    """
        == Claude ==
        
        gbmergeCID.groupby('Customer ID')['Sales Revenue'].sum().reset_index()
        ```
        It does two things:
        1. Converts the result into a **DataFrame**
        2. Pushes the index (in this case `Customer ID`) back into a regular column

        So before `reset_index()` you'd have:
        ```
        Customer ID        # <-- this is the index
        C001          100
        C002          200
        ```

        After `reset_index()` you'd have:
        ```
        Customer ID  Sales Revenue   # <-- both are now regular columns
        0        C001            100
        1        C002            200
    
    """

    revByCustMess = revByCustMess.merge(gbmergeMessy[['Customer ID','Cust_FName','Cust_LName']].drop_duplicates(),
                                        on='Customer ID',
                                        how='left')
    
    print(revByCustMess.head(3))

# Function Calls

#claude_Sheet2_Dup_UniqueCheck()

# s2_8bDCE = sheet2_Dup_Check(s2_8bDCE,'Customer ID','first')

# print(s1_8bDCE['Customer ID'])
# print(s2_8bDCE.head(2))

    # Remove Duplicate Rows from sheet 2 and reassign to sheet 2
        # The function has a return value which needs to be assigned back to the df.
        # Hence why s2_8bDCE = the function

s2_8bDCE = sheet2_Dup_Check(s2_8bDCE,'Customer ID')

# groupByChecks()

practiceGroupBy()











    # Scrap Code

'''
        == For old Code I may want to keep and reference to but no longer need ==


    Prints out duplicated rows in given sheet based on given Column Name

print(s2_8bDCE[s2_8bDCE['Customer ID'].duplicated(keep=False)].sort_values('Customer ID'))


# print(s2_8bDCE[s2_8bDCE['Cust_FName'] == 'sample'])

'''

