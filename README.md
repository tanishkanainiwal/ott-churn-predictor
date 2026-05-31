# OTT Churn Predictor & Revenue Impact Analysis

## Problem Statement
OTT platforms face massive subscriber churn. This project predicts which users will cancel their subscription and calculates the exact revenue impact.

## Key Findings
- Churn Rate: 50.3% (industry average: 6-8%)
- Monthly Revenue at Risk: $33,009
- Yearly Revenue at Risk: $396,118 (~₹3.28 Crore)
- High Risk Users: 2,457 users = $32,200/month at risk
- Retention Strategy ROI: $12,880/month saved with 20% discount offer

## What Makes This Project Unique
- Revenue Impact Calculator — exact dollar loss quantified
- User Risk Segmentation — High/Medium/Low risk buckets
- SHAP Explainability — WHY each user will churn
- Retention Strategy with ROI — business recommendation with numbers
- Live Streamlit App — real-time churn prediction

## Tech Stack
Python, Pandas, XGBoost, SHAP, Streamlit

## ML Models
| Model | Accuracy | AUC-ROC |
|---|---|---|
| Logistic Regression | 88% | 0.959 |
| Random Forest | 98% | 0.998 |
| XGBoost | 99% | 1.000 |

## Top Churn Predictors (SHAP)
1. avg_watch_time_per_day
2. last_login_days
3. watch_hours

## Live Demo
Coming soon

## Dataset
Kaggle — Netflix Customer Churn by Abdul Wadood
