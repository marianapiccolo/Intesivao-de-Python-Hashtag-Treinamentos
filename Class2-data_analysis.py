#!/usr/bin/env python
# coding: utf-8


#Informations and data: 
https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers

""""

The situation:

Analyzing the historic of the customers of the last years, you
noticed that more than 26% of the customers who entered the
company, canceled the contract.
The only information you have is a .csv file extracted from the
company system (shown at the side).

""""

# Steps:
# Step 1 - Import data base
# Step 2 - Cleaning data base
# Step 3 - Simple Analysis
# Step 4 - Graphical analysis
# Step 5 - Conclusions and analys


# Step 1 - Import data base
import pandas as pd

df = pd.read_csv("telecom_users.csv")
table = df.drop(['Unnamed: 0'], axis = 1) #Column with messy data. It was deleted.
display(table)


# Treatment and vision data overview

# Step 2 - Cleaning data base
print(table.info())

# See if there is and adjust any value being misrecognized 
table["TotalGasto"] = pd.to_numeric(table["TotalGasto"], errors = "coerce")

# See if there are empty columns
table = table.dropna(how = "all", axis = 1) # delete empty columns with all empty value

# See if there are empty values 
table = table.dropna(how = "any", axis = 0) # delete rows with any empty value


# Step 3 - Simple Analysis - See how company cancellations are behaving
print(table["Churn"].value_counts()) # count how many customers canceled and how many did not cancel
print(table["Churn"].value_counts(normalize = True).map("{:.1%}".format)) # percentage


# Step 4 - Graphical analysis 
# !pip install plotly
import plotly.express as px

#for each column of the database, compare with the cancellation and create a graph
for column in table.columns:
    print(column)
    graphic = px.histogram(table, x = column, color = "Churn") #Color = different colors for different values of the column 'Churn'
    graphic.show()


# Step 5 - Conclusions and analysis - understanding the cause of cancellations and finding possible solutions

# - Larger families tend to cancel less. - Graphics Casado (Married) and Dependentes (Dependents) -
#   - We can offer a second number for free to the customer or a family plan.

# - The longer as a customer, the less chance you have of canceling. - Graphic MesesComoCliente = Months as a customer -
#   - In the first few months customers cancel a lot
#   - There may be problem at the beginning of the customer period
#   - There may be bad marketing action

# - There is a problem with Fiber, customers cancel a lot. - Graphic ServicoInternet -
#   - It is necessary to look carefully at the cause of this problem

# - The fewer services a person has, the greater the chance of them canceling. - Service graphics -
#   - We can provide a free service to the person

# - We can encourage direct debit or card payments, much lower cancellation fees - Graphic FormaPagamento = Form of payment -

# - We can offer annual contract incentives

