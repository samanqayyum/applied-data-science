

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing files of four companies
BCS_share_price = pd.read_csv("BCS_ann.csv")
BP_share_price = pd.read_csv("BP_ann.csv")
TESCO_share_price = pd.read_csv("TSCO_ann.csv")
VOD_share_price = pd.read_csv("VOD_ann.csv")
print(BCS_share_price)
print(BP_share_price)
print(TESCO_share_price)
print(VOD_share_price)


#subplots of four companies
plt.figure()

#subplot of Barclays
plt.subplot(2,2,1)
plt.hist(BCS_share_price['ann_return'], label="BCS")
plt.legend()

#subplot of BP
plt.subplot(2,2,2)
plt.hist(BP_share_price['ann_return'], label="BP")
plt.legend()

#subplot of Tesco
plt.subplot(2,2,3)
plt.hist(TESCO_share_price['ann_return'], label="TESCO")
plt.legend()

#subplot of Vodaphone
plt.subplot(2,2,4)
plt.hist(VOD_share_price['ann_return'], label="VOD")
plt.legend()
plt.savefig("four_hist.png")
plt.show()

#creating combined histogram of two companies
plt.hist(BP_share_price['ann_return'], label="BP", density=True, alpha=0.7)
plt.hist(TESCO_share_price['ann_return'], label="TESCO", density=True, alpha=0.7)
plt.legend()
plt.xlabel("ann_return")
plt.ylabel("year_in_percent")
plt.savefig("one_hist.png")
plt.show()

#creating a box plot of all companies
company_names = ["Barclays","BP","Tesco","Vodaphone"]
companies_return = [BCS_share_price["ann_return"],BP_share_price["ann_return"],
                    TESCO_share_price["ann_return"],VOD_share_price["ann_return"]]
plt.boxplot(companies_return, labels=company_names)
plt.legend()
plt.xlabel("company_names")
plt.ylabel("ann_return")
plt.savefig("box_plot.png")
plt.show()

#creating pie chart without normalisation
company_names = ["Barclays","BP","Tesco","Vodaphone"]
market_capitalisation = np.array([33367,68785,20979,29741])
plt.figure()
plt.pie(market_capitalisation, labels=company_names)
plt.show()

#creating pie chart with normalisation
company_names = ["Barclays","BP","Tesco","Vodaphone"]
market_capitalisation = np.array([33367,68785,20979,29741])
FTSE = 1814000
normalisation = market_capitalisation/FTSE
plt.figure()
plt.pie(normalisation, labels=company_names, normalize=False)
plt.show()

#creating a bar plot
company_names = ["Barclays","BP","Tesco","Vodaphone"]
market_capitalisation = np.array([33367,68785,20979,29741])
plt.figure()
plt.bar(company_names,market_capitalisation)
plt.xlabel("company_names")
plt.ylabel("market_capitalisations")
plt.show()
