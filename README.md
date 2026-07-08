# OTT Subscription Churn Prediction & Revenue Impact Analysis

## Problem Statement

OTT (streaming) platforms lose revenue when subscribers cancel — this is called **churn**. This project predicts which users are likely to churn, quantifies the exact revenue impact, and identifies *why* users churn using explainability techniques.

## Dataset

- **Source:** Kaggle — "Netflix Customer Churn" by Abdul Wadood
- **Size:** 5,000 customer records, 14 columns
- **Features:** age, gender, subscription type, watch hours, last login days, region, device, monthly fee, payment method, number of profiles, avg watch time/day, favorite genre
- **Target:** `churned` (0 = active, 1 = churned)
- **Missing values:** None — dataset was clean, verified with `df.isnull().sum()`

## Key Findings

| Metric | Value |
|---|---|
| Churn Rate | 50.3% (2,515 of 5,000 users) — vs industry average of 6-8% |
| Monthly Revenue at Risk | $33,009.85 |
| Yearly Revenue at Risk | $396,118.20 (~₹3.28 Crore) |
| High-Risk Users (churn probability > 0.7) | 2,457 users, $32,200.43/month at risk |
| Estimated Retention Savings | $12,880.17/month if 50% of high-risk users retained via 20% discount |

## Approach

### 1. Exploratory Data Analysis
Built 6 visualizations to understand churn drivers:
- Churn distribution (overall class balance)
- Churn rate by subscription type (Basic subscribers churn most)
- Days since last login vs churn (longer gap → higher churn)
- Watch hours vs churn (lower engagement → higher churn)
- Monthly fee vs churn (higher fee → higher churn tendency)
- Churn rate by region (Europe highest)

### 2. Revenue Impact Analysis
Grouped churned users by subscription type and region to break down exactly where revenue loss is concentrated — not just an aggregate number, but a segment-level view a business team could act on.

### 3. Machine Learning Models
Three models were trained and compared on a stratified 80/20 train/test split:

| Model | Accuracy | AUC-ROC |
|---|---|---|
| Logistic Regression | 88% | 0.959 |
| Random Forest | 98% | 0.998 |
| XGBoost | 99% | 1.000 |

### 4. Explainability (SHAP)
Used SHAP's `TreeExplainer` on the XGBoost model to identify which features most influenced individual churn predictions, rather than relying on a single global feature-importance number. Top predictors:
1. `avg_watch_time_per_day`
2. `last_login_days`
3. `watch_hours`

### 5. Risk Segmentation
Used the Random Forest model's predicted probabilities to bucket users into Low (<0.3), Medium (0.3–0.7), and High (>0.7) risk groups, then quantified revenue at risk per segment — turning a raw prediction into a business-actionable output.

### 6. Power BI Dashboard
Built an interactive Power BI dashboard for a business-facing view of the same data — designed for stakeholders who need to explore churn patterns without touching code or notebooks.

**Includes:**
- KPI cards — Total Customers (5000), Churned Customers (2515), Active Customers (2485), Churn Rate (50.30%), Average Monthly Fee (13.68)
- Churn Rate % by Subscription Type — Basic churns highest (~62%), Premium lowest
- Churn Rate % by Region — Europe highest, Africa lowest
- Average Watch Hours by Churn Status — Active users watch roughly 2x more than churned users
- Average Last Login Days by Churn Status — churned users had gone nearly 2x longer without logging in
- Interactive filters for subscription type, region, and device

## Tech Stack

Python, Pandas, Scikit-learn, XGBoost, SHAP, Matplotlib, Seaborn, Power BI

## Dataset Source

Kaggle — [Netflix Customer Churn](https://www.kaggle.com) by Abdul Wadood
