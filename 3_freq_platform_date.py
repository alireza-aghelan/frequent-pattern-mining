
import numpy as np
import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt

divar_data = pd.read_csv("./divar_posts_dataset.csv")

divar_data = divar_data.dropna(subset=['created_at','platform'])

list_col = divar_data['created_at'].tolist()

days = []
for item in list_col:

    string = item
    x = string.split(" ")
    day = x[0]
    days.append(day)

divar_data['created_day'] = days
selected_cols = divar_data[['created_day','platform']]

records = []
records = selected_cols.values.tolist()

association_rules = apriori(records, min_support=0.05, min_confidence=0.2, min_lift=0.99)
association_results = list(association_rules)

list_date_dup = divar_data['created_day'].values.tolist()
list_date = list(set(list_date_dup))

list_platform_dup = divar_data['platform'].values.tolist()
list_platform = list(set(list_platform_dup))

print("")
print("===================================== Date-->Platform =====================================")
print("")

for item in association_results:

    pair = item[0]
    items = [x for x in pair]

    if len(items) == 2:

        if (items[0] in list_date):

         print("Rule: " + items[0] + " -> " + items[1])
         print("Support: " + str(item[1]))
         print("Confidence: " + str(item[2][0][2]))
         print("Lift: " + str(item[2][0][3]))
         print("=====================================")


print("")
print("===================================== Platform-->Date =====================================")
print("")

for item in association_results:

    pair = item[0]
    items = [x for x in pair]

    if len(items) == 2:

        if (items[0] in list_platform):

         print("Rule: " + items[0] + " -> " + items[1])
         print("Support: " + str(item[1]))
         print("Confidence: " + str(item[2][0][2]))
         print("Lift: " + str(item[2][0][3]))
         print("=====================================")






