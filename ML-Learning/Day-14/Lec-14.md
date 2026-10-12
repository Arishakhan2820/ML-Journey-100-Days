# Day 13: How to Frame a Machine Learning Problem (Project Planning) 🚀

> **Context:** As a junior data scientist, you often get small, specific tasks (like cleaning data or training a specific model). But as you grow into leadership roles, your success depends on your ability to translate vague **Business Problems** into structured, solvable **Machine Learning Problems**.

---

## 1. The Core Objective: Business vs. ML Problem

* **Business Problem:** High-level strategic goal (e.g., *"Netflix revenue is dropping; we need to increase profit"*).
* **Machine Learning Problem:** Converting that goal into a clear mathematical/predictive target (e.g., *"Predict user churn probability so we can intervene before they cancel"*).

---

## 2. Step-by-Step Framework for Framing ML Problems

### Step 1: Translate Business Goal to ML Metric
* **Example Case (Netflix):**
  * **Goal:** Increase Revenue.
  * **Strategy:** Reduce **Churn Rate** (the percentage of subscribers cancelling their membership).
  * **ML Objective:** Identify *which* users are likely to churn in the next 30 days and assign a churn probability score ($0$ to $100\%$).

### Step 2: Define Problem Type & Output
* **Is it Classification or Regression?**
  * *Simple Approach (Classification):* Binary classification $\rightarrow$ Will user churn? ($\text{Yes} = 1, \text{No} = 0$).
  * *Better Approach (Regression/Probability):* Predict the **Probability Score** ($\text{Churn Prob} = 85\%$). Higher risk users get larger discount offers, while low-risk users get smaller incentives to save costs.

### Step 3: Evaluate Current / Existing Solutions
* Check how the business currently solves this (e.g., heuristic rule-based logic like *"If inactive for 14 days, send email"*).
* Understanding baseline performance gives you a benchmark to beat with your ML model.

### Step 4: Identify Required Data & Feasibility
* Collaborate with **Data Engineers** to see what data is actually logged and stored:
  * **Watch Time / Engagement:** Total hours streamed, browsing vs. watching ratio.
  * **Search Behavior:** Number of unfulfilled searches (user searched for movies not available on the platform).
  * **Drop-off Rates:** Number of titles started but abandoned within 10 minutes.

### Step 5: Define Success Metrics
* Establish clear offline and business metrics:
  * **Technical Metric:** ROC-AUC / Precision-Recall curve (to handle class imbalance).
  * **Business Metric:** Reduction in monthly user churn rate (e.g., dropping from $4.0\%$ to $3.75\%$).

### Step 6: Choose Learning Pipeline Strategy
* **Batch (Offline) vs. Online Learning:**
  * *Offline / Batch Learning:* Retrain the model on user data periodically (e.g., weekly/monthly).
  * *Online Learning:* Retrain continuously on live streaming logs (more complex, used for highly volatile trends).

### Step 7: Validate Key Assumptions
* Test critical assumptions before writing code:
  * Are these features available in production in real-time?
  * Will one universal model work globally, or do we need region-specific models (US vs. Asia)?

---

## 💡 Modern Update (Looking toward 2027)
* **Automated Feature Stores & MLOps:** Modern ML planning heavily relies on **Feature Stores** (e.g., Feast, Hopsworks) to ensure features computed during batch training are identical to those served in production APIs, avoiding data leakage and feature drift.
