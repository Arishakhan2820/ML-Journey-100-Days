# Machine Learning Development Life Cycle (MLDLC) - Day 09 🚀

> **Note:** These concise notes cover Day 09 of CampusX's ML series. While previous days focused on "What" and "Why", this marks the shift to **"How"** we build end-to-end production-ready ML software.

---

## 1. What is MLDLC?
Just like Software Engineering uses **SDLC** (Software Development Life Cycle) to build software from scratch, Data Science uses **MLDLC**—a set of standard guidelines and steps to take an ML project from a raw idea to a deployed production product.

---

## 2. The 9 Steps of MLDLC

### 1. Framing the Problem
* Define the exact business problem, identify who the users are, determine constraints, and decide whether to use Supervised or Unsupervised learning.

### 2. Gathering Data
* Collecting raw data from various sources such as CSV files, corporate databases, APIs, or via **Web Scraping** (e.g., pulling live product prices or hotel listings).

### 3. Data Preprocessing (Data Cleaning)
* Cleaning the messy data by handling missing values, removing duplicates, correcting errors, and performing **Feature Scaling** so algorithms can process numerical values smoothly.

### 4. Exploratory Data Analysis (EDA)
* Analyzing data patterns by plotting graphs and running Univariate, Bivariate, and Multivariate analysis to understand relationships between input columns and outputs.

### 5. Feature Engineering & Selection
* **Engineering:** Creating new, meaningful columns (e.g., combining rooms and bathrooms into "Square Feet") to make predictions easier.
* **Selection:** Dropping irrelevant features to reduce training time and improve model performance.

### 6. Model Training & Evaluation
* Training multiple machine learning algorithms (e.g., Logistic Regression, Decision Trees, Ensemble models) and evaluating them using performance metrics (Accuracy, Mean Squared Error, etc.) to pick the best one.

### 7. Model Deployment
* Converting the trained model into a binary file (e.g., via `pickle`), wrapping it into an API, and hosting it on cloud servers (AWS, GCP, Render) so users can interact with it via web or mobile apps.

### 8. Testing (Beta Testing)
* Releasing the model to a small group of trusted or loyal customers first to gather feedback and check for hidden bugs.

### 9. Monitoring & Optimization
* Launching the product to all users, setting up server load balancing, and tracking model performance over time.

---

## 💡 Modern Update (Looking toward 2027)
* **The Rise of MLDLC Automation & MLOps:** In modern workflows (approaching 2027), steps 7 through 9 are rarely done manually. **MLOps platforms** (like MLflow, Kubeflow, and Streamlit Cloud) automate continuous retraining, model tracking, and deployment to prevent model drift (performance decay over time).
