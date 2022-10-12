
import numpy as np
import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt

divar_data = pd.read_csv("./divar_posts_dataset.csv")

divar_data = divar_data.dropna(subset=['cat3','cat2'])

divar_data['full cat'] = divar_data['cat1'].map(str) + ' + ' + divar_data['cat2'].map(str) + ' + ' + divar_data['cat3'].map(str)

selected_cols1 = divar_data[['cat1','city']]
selected_cols2 = divar_data[['cat2','city']]
selected_cols3 = divar_data[['full cat','city']]

records1 = []
records1 = selected_cols1.values.tolist()

records2 = []
records2 = selected_cols2.values.tolist()

records3 = []
records3 = selected_cols3.values.tolist()

association_rules1 = apriori(records1, min_support=0.001, min_confidence=0.2, min_lift=1.0001)
association_results1 = list(association_rules1)

association_rules2 = apriori(records2, min_support=0.001, min_confidence=0.2, min_lift=1.0001)
association_results2 = list(association_rules2)

association_rules3 = apriori(records3, min_support=0.005, min_confidence=0.2, min_lift=1.0001)
association_results3 = list(association_rules3)

list_city_dup = divar_data['city'].values.tolist()
list_city = list(set(list_city_dup))

list_cat1_dup = divar_data['cat1'].values.tolist()
list_cat1 = list(set(list_cat1_dup))

list_cat2_dup = divar_data['cat2'].values.tolist()
list_cat2 = list(set(list_cat2_dup))

list_full_cat_dup = divar_data['full cat'].values.tolist()
list_full_cat = list(set(list_full_cat_dup))


print("")
print("===================================== City-->Full Cat =====================================")
print("")

for item in association_results3:

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
print("===================================== Full Cat-->City =====================================")
print("")

for item in association_results3:

    pair = item[0]
    items = [x for x in pair]

    if len(items) == 2:

        if (items[0] in list_full_cat):

            print("Rule: " + items[0] + " -> " + items[1])
            print("Support: " + str(item[1]))
            print("Confidence: " + str(item[2][0][2]))
            print("Lift: " + str(item[2][0][3]))
            print("=====================================")


print("")
print("===================================== City-->Cat1 =====================================")
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
print("===================================== Cat1-->City =====================================")
print("")

for item in association_results1:

    pair = item[0]
    items = [x for x in pair]

    if len(items) == 2:

        if (items[0] in list_cat1):

            print("Rule: " + items[0] + " -> " + items[1])
            print("Support: " + str(item[1]))
            print("Confidence: " + str(item[2][0][2]))
            print("Lift: " + str(item[2][0][3]))
            print("=====================================")


print("")
print("===================================== City-->Cat2 =====================================")
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

print("")
print("===================================== Cat2-->City =====================================")
print("")

for item in association_results2:

    pair = item[0]
    items = [x for x in pair]

    if len(items) == 2:

        if (items[0] in list_cat2):

            print("Rule: " + items[0] + " -> " + items[1])
            print("Support: " + str(item[1]))
            print("Confidence: " + str(item[2][0][2]))
            print("Lift: " + str(item[2][0][3]))
            print("=====================================")
