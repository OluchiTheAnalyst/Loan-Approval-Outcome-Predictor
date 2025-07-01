# Loan-Approval-Outcome-Predictor

## Project Overview
This project is aimed to build a predictive Machine Learning model for real-time user interaction. New users can input their details,and the trained model analyzes the new input by comparing it to what it has learned from past data, then it makes an intelligent decision using Streamlit.

## Data Source
The data is a "Banking data.xlsx" file containing 5,000 customer records from a banking institution, capturing demographic details, financial behavior, credit card usage, and loan history. These insights enabled both historical analysis and predictive modeling.

## Tools
 - Microsoft Excel: This tool was used for
    - Data cleaning

 - Python(Pandas) : This tool was used for
    - Exploratory data analysis
    - Outlier detection and Removal
    - Innovative Feature Engineering
    - Creation of Binary Target
    - Building and Comparing models
    - Model Evaluation
    - Creation of Feature Importance
  
## Exploratory Data analysis
For EDA, Python was used to inspect distributions, identify outliers, and flag missing values in key fields like Loan Amount, Credit Limit, and Installment Amount. Boxplots and histograms helped visualize imbalances and detect anomalies.
This structured approach laid the foundation for building an accurate, responsive model and an insightful dashboard that supports informed decision-making around loan approvals.

## Data Preprocessing
To prepare the data for modeling, the following preprocessing steps were carried out using Python;
- Categorical Encoding:
The target variable was binary-encoded into:
  - Qualified Approval = 1
  - Rejected or Not Qualified = 0
- Feature Scaling:
  - I Applied StandardScaler to normalize numeric features and prevent scale dominance in distance-based algorithms.
- Balancing the Dataset:
  - I Implemented SMOTE (Synthetic Minority Oversampling Technique) to address class imbalance, especially after converting the target to binary.

## Feature Engineering
The dataset was enriched with domain-informed engineered features:
- Monthly Installment: It tells us the amount of money the borrower agrees to pay back monthly. 
  - `Monthly Installment: Loan Amount / Loan Term `

- Debt Burden Score: It tells us how heavy the borrower's money problems are. The higher the DBS, the less likely the loan will be approved
    - `Debt Burden Score = Loan Amount + Credit Card Balance / Account Balance (Income)`

- Credit Usage Ratio (CUR) Score: It tells us how much money the borrower has spent from their Credit Limit. It tells us the percentage of available credit that the borrower is currently using.
    - `Credit Usage Ratio = Credit Card Balance / Credit Limit`
If CUR is:
  - Low: You're not spending much (score = 0)
  - Moderate: You’re spending a bit more (score = 1)
 - Over the Limit: You’re Spending too fast! (score = 2)

```
 #Monthly Installment
df['Monthly_Installment'] = df['Loan Amount'] / df['Loan Term']

# CUR Score
df['CUR_Score'] = df['CUR Category'].map({'Over the Limit': 2, 'Moderate': 1, 'Low': 0})

 #Credit Usage Ratio
df['Credit_Usage_Ratio'] = df['Credit Card Balance'] / (df['Credit Limit'] + 1)

#Debt Burden Score
df['Debt_Burden_Score'] = (df['Loan Amount'] + df['Credit Card Balance']) / (df['Account Balance'] + 1)

#Trust Index
df['Trust_Index'] = (df['Account Age (Years)'] * df['Credit Limit']) / (df['Loan Amount'] + 1)
```

Trust Index: This tells the bank how trustworthy the borrower is.
  - If they’ve had their account for a long time.
  - And have a high spending limit.
  - And haven’t borrowed too much. (High score = high trust)
  - The higher the score, the more trustworthy the customer

Quality Approval: This tells us if the borrower is likely to be approved for a loan if they meet the following conditions;
  - If they have approved or closed a loan before
  - If they are not using too much credit (low/moderate)
  - If they don’t owe too much money outside the loan 
  - If they have had their account for more than 2 years.
  - If they meet all these conditions, they will be approved for the loan; otherwise, they will not be approved

## Modelling Approach
We used a Random Forest Classifier due to its robustness, interpretability, and ability to handle mixed feature types.

- Key Configuration:
  - Class weight = 'balanced'
  - Random state = 0 for reproducibility
  - Used SMOTE-balanced training data

- Evaluation Metrics:
  - Accuracy: 96.1%
  - Precision (Qualified): 0.70
   - Recall (Qualified): 0.93
   - F1-score (Qualified): 0.80
 ![Screenshot (399)](https://github.com/user-attachments/assets/246bc16d-4fe0-4a1c-953c-c630edcd445e)

## USING STREAMLIT TO BUILD A REAL-TIME LOAN APPROVAL PREDICTOR
I built a web app called [“Loan Approval Outcome Predictor”](https://loan-approval-outcome-predictor-4sritgbgrsnegffcuhqgzy.streamlit.app/) using Streamlit and a machine learning model. Users can input banking data like loan amount, interest rate, and account age to receive and the trained model analyzes the new input by comparing it to what it has learned from past data, then it makes an intelligent decision!. The app uses widgets for input, a structured layout with `st.columns`, and is styled in dark mode. It’s responsive and user-friendly and was deployed on Streamlit Cloud for easy public access and testing.


     
