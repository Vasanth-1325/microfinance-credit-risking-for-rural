import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

st.set_page_config(page_title="Microfinance Credit Risking", layout="wide")

st.title("Microfinance Credit Risking for Rural Borrowers")

st.write(
"Enter weekly farmer revenues. If some weeks are missing, enter **0**. "
"The system will predict missing values using **ARIMA forecasting** and evaluate loan eligibility."
)

# Input weekly revenues
revenues = []

st.subheader("Enter Farmer Weekly Revenues")

for i in range(1,13):
    val = st.number_input(f"Week {i} Revenue (0 if missing)", min_value=0.0)
    revenues.append(val)

# Button
if st.button("Evaluate Loan Eligibility"):

    df = pd.DataFrame({
        "Week": np.arange(1,13),
        "Revenue": revenues
    })

    # Detect missing weeks
    missing_mask = df["Revenue"] == 0
    df.loc[missing_mask, "Revenue"] = np.nan

    # Interpolate existing values
    series = df["Revenue"].interpolate()

    # ARIMA Model
    model = ARIMA(series, order=(1,1,1))
    model_fit = model.fit()

    # Predict all weeks
    predictions = model_fit.predict(start=0, end=11)

    df["Predicted Revenue"] = predictions

    # Replace missing with predicted values
    df["Final Revenue"] = df["Revenue"]
    df.loc[df["Final Revenue"].isna(), "Final Revenue"] = df["Predicted Revenue"]

    # Financial analysis
    avg_revenue = df["Final Revenue"].mean()
    std_dev = df["Final Revenue"].std()

    value_score = avg_revenue / 1000
    stability_score = 1/(1+std_dev)

    farmer_rating = value_score + stability_score

    credit_score = int(300 + farmer_rating*100)

    # Credit score classification
    if credit_score >= 750:
        range_text = "750 - 850"
        score_category = "Excellent"
        risk = "Low Risk"
        decision = "Loan Approved"
        loan_amt = avg_revenue * 0.30 * 13

    elif credit_score >= 700:
        range_text = "700 - 749"
        score_category = "Good"
        risk = "Low Risk"
        decision = "Loan Approved"
        loan_amt = avg_revenue * 0.25 * 13

    elif credit_score >= 650:
        range_text = "650 - 699"
        score_category = "Fair"
        risk = "Medium Risk"
        decision = "Loan Approved"
        loan_amt = avg_revenue * 0.20 * 13

    elif credit_score >= 600:
        range_text = "600 - 649"
        score_category = "Poor"
        risk = "High Risk"
        decision = "Loan Rejected"
        loan_amt = avg_revenue * 0.10 * 13

    else:
        range_text = "Below 600"
        score_category = "Very Poor"
        risk = "High Risk"
        decision = "Loan Rejected"
        loan_amt = 0

    st.subheader("Loan Evaluation Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Average Revenue", round(avg_revenue,2))
        st.metric("Credit Score", credit_score)
        st.write("Credit Score Range:", range_text)
        st.write("Score Category:", score_category)

    with col2:
        st.write("Risk Category:", risk)
        st.write("Recommended Loan Amount:", round(loan_amt,2))
        st.write("Loan Decision:", decision)

    # Show predicted missing values
    st.subheader("Predicted Values for Missing Weeks")

    missing_weeks = df[df["Revenue"].isna()][["Week","Final Revenue"]]
    if len(missing_weeks) > 0:
        st.dataframe(missing_weeks)
    else:
        st.write("No missing weeks detected.")

    # Revenue graph
    st.subheader("Revenue Trend Analysis")

    fig, ax = plt.subplots()

    ax.plot(df["Week"], df["Final Revenue"], marker='o', label="Final Revenue")

    ax.scatter(
        df["Week"][missing_mask],
        df["Final Revenue"][missing_mask],
        color="red",
        s=100,
        label="Predicted Missing Values"
    )

    ax.set_title("Weekly Revenue with Predicted Missing Values")
    ax.set_xlabel("Week")
    ax.set_ylabel("Revenue")
    ax.legend()

    st.pyplot(fig)

    # Full dataset
    st.subheader("Complete Revenue Analysis Table")

    st.dataframe(df)