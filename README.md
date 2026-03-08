# microfinance-credit-risking-for-rural
👨‍💻 Author

Ravi Vasanth Kumar
B.Tech Final Year – Computer Science and Engineering
Indian Institute of Information Technology Design and Manufacturing, Kurnool

---

# 📌 Project Overview

Microfinance institutions provide loans to rural borrowers such as farmers and small business owners.
However, identifying **high-risk borrowers** is challenging due to limited financial history.

This project builds a **data-driven credit risk prediction system** that analyzes **weekly revenue trends** of farmers and predicts their creditworthiness using **time series forecasting and machine learning techniques**.

The system helps microfinance institutions:

* Predict **borrower risk levels**
* Generate **credit scores**
* Estimate **default probability**
* Recommend **loan approval and loan amount**

---

# 🚀 Features

* Weekly revenue trend analysis
* Missing week prediction using **ARIMA forecasting**
* Automated **credit score generation**
* **Risk category classification**
* **Loan eligibility prediction**
* **Default probability estimation**
* Interactive **data visualization dashboard**

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* ARIMA (Time Series Forecasting)
* Scikit-learn
* Matplotlib
* Flask
* Jupyter Notebook

---

# 📊 Dataset

The dataset contains **weekly revenue records of rural farmers**.

It includes:

* Weekly income values
* Stability trend score
* Value score
* Farmer rating
* Loan eligibility indicators

These features are used to **predict financial stability and credit risk**.

---

# ⚙️ Methodology

The system follows these steps:

1. **Data Preprocessing**

   * Clean and normalize weekly revenue data.

2. **Time Series Forecasting**

   * Use **ARIMA model** to predict missing or future revenue values.

3. **Feature Engineering**

   * Compute:
   * Value Score
   * Stability Trend Score
   * Farmer Rating

4. **Credit Score Calculation**

   * Generate a credit score based on revenue stability and income trends.

5. **Risk Classification**

   * Categorize borrowers into:

     * Low Risk
     * Medium Risk
     * High Risk

6. **Loan Recommendation**

   * Estimate loan eligibility and recommended loan amount.

---

# 📈 Outputs

The system produces the following results:

* **Credit Score**
* **Risk Category**
* **Default Probability**
* **Loan Approval Decision**
* **Recommended Loan Amount**
* **Revenue Trend Graphs**

---

# ▶️ How to Run the Project

### Clone the Repository

git clone https://github.com/Vasanth-1325/microfinance-credit-risking-for-rural.git

### Install Dependencies

pip install -r requirements.txt

### Run the Application

python app.py

