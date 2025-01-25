import pandas as pd
"""
def claen_and_update(input_file,output_file):
    df = pd.read_csv(input_file)
    
    #print(df.duplicated())

    #droping duplicate if any
    df.drop_duplicates(inplace=True)

    #handling missing values
    #print(df.isnull().sum())
    df["price"].fillna(0,inplace=True)

    #handling wrong data
    df.loc[13,"engine-type"] = "ohc"
    for x in df.index:
        df.loc[x,"index"] = x
    
    #saving the file
    df.to_csv(output_file,index=False)

input = "automobile_data.csv"
output = "cleaned_data.csv"
claen_and_update(input,output)
"""

df = pd.read_csv("cleaned_data.csv")
#printing first and last five rows
#print(df.head())
#print(df.tail())

#printing toyota car detalis
toyota_car = df["company"]=="toyota"
#print(df[toyota_car])

#car count per company
car_count = df["company"].value_counts()
#print(car_count)

#highest price
highest_price = df.groupby("company")["price"].max()
#print(highest_price)

#average-milege
avg = df.groupby("company")["average-mileage"].mean()
#print(avg)

#sorting in descending order
sort = df.sort_values(by="price",ascending=False)
#print(sort)

#most expensive company
most_expensive = df.loc[df['price'].idxmax(), 'company']
print(most_expensive)
#my name is deepak


