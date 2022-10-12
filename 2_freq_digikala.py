
import numpy as np
import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt

digikala_data = pd.read_csv("./orders.csv")

digikala_data["city_name_fa"].replace({"تهران": "Tehran", "مشهد": "Mashhad", "اصفهان": "Isfahan", "کرج": "Karaj", "شیراز": "Shiraz", "اهواز": "Ahvaz", "کرمانشاه": "kermanshah", "تبریز": "Tabriz", "قم": "Qom"}, inplace=True)

list_col_id = digikala_data['ID_Item'].tolist()

ID_Itemstr = []
for item in list_col_id :

    itemint = item
    itemstr = str(itemint)
    ID_Itemstr.append( itemstr)

digikala_data['ID_Itemstr'] = ID_Itemstr

list_col_date = digikala_data['DateTime_CartFinalize'].tolist()

years = []
for item in list_col_date :

    string = item
    x = string.split(" ")
    date = x[0]
    y = date.split("-")
    year = y[0]
    years.append(year)

digikala_data['year'] = years

selected_cols1 = digikala_data[['city_name_fa','ID_Itemstr']]
selected_cols2 = digikala_data[['city_name_fa','year']]

records1 = []
records1 = selected_cols1.values.tolist()

records2 = []
records2 = selected_cols2.values.tolist()

association_rules1 = apriori(records1, min_support=0.0003, min_confidence=0.2, min_lift=1.0001)
association_results1 = list(association_rules1)

association_rules2 = apriori(records2, min_support=0.003, min_confidence=0.2, min_lift=1.0001)
association_results2 = list(association_rules2)

list_city_dup = digikala_data['city_name_fa'].values.tolist()
list_city = list(set(list_city_dup))

list_id_item_dup = digikala_data['ID_Itemstr'].values.tolist()
list_id_item = list(set(list_id_item_dup))

list_year_dup = digikala_data['year'].values.tolist()
list_year = list(set(list_year_dup))


print("")
print("===================================== City-->ID_Item =====================================")
print("")

for item in association_results1:

    pair = item[0]
    items = [x for x in pair]

    if len(items) == 2:

        if (items[0] in list_city):

         print("Rule: " + items[0] + " -> " + items[1])
         print("Support: " + str(item[1]))
         print("Confidence: " + str(item[2][0][2]))
         print("Lift: " + str(item[2][0][3]))
         print("=====================================")


print("")
print("===================================== ID_Item-->City =====================================")
print("")

for item in association_results1:

    pair = item[0]
    items = [x for x in pair]

    if len(items) == 2:

        if (items[0] in list_id_item):

         print("Rule: " + items[0] + " -> " + items[1])
         print("Support: " + str(item[1]))
         print("Confidence: " + str(item[2][0][2]))
         print("Lift: " + str(item[2][0][3]))
         print("=====================================")


print("")
print("===================================== Year-->City =====================================")
print("")

for item in association_results2:

    pair = item[0]
    items = [x for x in pair]

    if len(items) == 2:

        if (items[0] in list_year):

         print("Rule: " + items[0] + " -> " + items[1])
         print("Support: " + str(item[1]))
         print("Confidence: " + str(item[2][0][2]))
         print("Lift: " + str(item[2][0][3]))
         print("=====================================")


print("")
print("===================================== City-->Year =====================================")
print("")

for item in association_results2:

    pair = item[0]
    items = [x for x in pair]

    if len(items) == 2:

        if (items[0] in list_city):

         print("Rule: " + items[0] + " -> " + items[1])
         print("Support: " + str(item[1]))
         print("Confidence: " + str(item[2][0][2]))
         print("Lift: " + str(item[2][0][3]))
         print("=====================================")


