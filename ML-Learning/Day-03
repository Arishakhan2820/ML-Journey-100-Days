Types of Machine Learning :

Note: These notes are compiled from the third lecture of the 100 Days of ML series by CampusX. They explain the different types of machine learning based on the amount of supervision required.

1. Classification of Machine Learning Based on Supervision
Depending on the amount of external supervision required to train a machine learning algorithm, ML can be divided into 4 main categories:

* Supervised Machine Learning

* Unsupervised Machine Learning

* Semi-Supervised Machine Learning

* Reinforcement Learning

TYPES OF MACHINE LEARNING
                             │
       ┌─────────────────────┼─────────────────────┬──────────────────────┐
       ▼                     ▼                     ▼                      ▼
┌──────────────┐      ┌──────────────┐      ┌──────────────┐      ┌────────────────┐
│  Supervised  │      │ Unsupervised │      │     Semi     │      │  Reinforcement │
│   Learning   │      │   Learning   │      │  Supervised  │      │    Learning    │
└──────┬───────┘      └──────┬───────┘      └──────────────┘      └────────────────┘
       │                     │
       ├─ Regression         ├─ Clustering
       └─ Classification     ├─ Dimensionality Reduction
                             ├─ Anomaly Detection
                             └─ Association Rule Learning

2. Supervised Machine Learning:
Definition: Supervised learning happens when your dataset contains both Input and Output (Labels). The algorithm's goal is to learn the mathematical relationship between the input and the output so that it can predict outputs for future, unseen inputs.

Example: Imagine a dataset of 5,000 students where each record contains:

Inputs: IQ, CGPA

Output (Target): Placement status (Yes or No)

How it works: The model learns the underlying pattern from these inputs and outputs. If a new student comes with a specific IQ and CGPA, the trained model can accurately predict whether they will get placed or not.

Supervised Learning is further divided into two types:

A. Regression:
Definition: Used when the target/output variable is Numerical (continuous values).

Examples: Predicting house prices, salary packages, temperature, or stock market values.

B. Classification:
Definition: Used when the target/output variable is Categorical (discrete classes or labels).

Examples: Email spam detection (Spam vs Not Spam), student placement (Yes vs No), weather forecasting (Rain vs No Rain), or image recognition (Dog vs Cat).

3. Unsupervised Machine Learning:
Definition: In unsupervised learning, your dataset contains only Inputs. There are no output labels or targets provided. The algorithm must explore the data on its own to find hidden structures or patterns.

Unsupervised learning is categorized into 4 major types:

A. Clustering:
Definition: Grouping similar data points together based on their shared characteristics.

Use Case: Customer segmentation in e-commerce, grouping students based on their IQ and CGPA profiles.

B. Dimensionality Reduction:
Definition: Reducing a massive number of input columns (features) into a smaller set without losing vital information.

Why it's needed: High-dimensional data slows down algorithms and often contains redundant information. Techniques like PCA (Principal Component Analysis) combine related columns (e.g., combining "number of rooms" and "house volume" into a single feature called "space"). It is also widely used for high-dimensional data visualization (e.g., projecting high-dimensional image data into 2D or 3D space).

C. Anomaly Detection:
Definition: Detecting rare items, events, or observations that raise suspicions by differing significantly from the majority of the data.

Use Cases: Detecting credit card fraud, manufacturing defects, or network security intrusions.

D. Association Rule Learning:
Definition: Discovering interesting relations or frequent patterns among variables in large databases.

Classic Example (Beer and Diapers): Supermarket market basket analysis revealed that customers who bought baby diapers frequently bought beer as well. Placing them close to each other significantly boosted sales!

4. Semi-Supervised Machine Learning:
Definition: A hybrid approach used when data is mostly unlabeled, but a small portion of it is labeled.

Why it's needed: Labeling data manually (hiring humans to tag images or text) is expensive and time-consuming. Semi-supervised learning allows algorithms to use a tiny amount of labeled data to automatically guide learning across a massive pool of unlabeled data.

Real-world Example: Google Photos groups pictures of the same person together automatically using unsupervised clustering. Once you manually label just one photo ("This is Dad"), it automatically tags all the other photos of that person.

5. Reinforcement Learning:
Definition: In this approach, no dataset is provided at all. Instead, an Agent interacts with an Environment from scratch, learning entirely through trial and error.

How it Works: * The agent takes actions within an environment.

Based on the action, it receives Rewards (for good moves) or Penalties / Punishments (for bad moves).

The agent updates its internal strategy (Policy) over time to maximize cumulative rewards and minimize penalties.

Real-world Applications: Self-driving cars, robotics, and advanced game-playing AI (such as Google DeepMind's AlphaGo, which beat human champions in complex games).

Quick Summary Table
Type of ML	Data Provided	Key Sub-categories	Main Goal
Supervised	Input + Output Labels	Regression, Classification	Predict a target label or value
Unsupervised	Input Only	Clustering, Dimensionality Reduction, Anomaly Detection, Association	Find hidden patterns or structures
Semi-Supervised	Mostly Unlabeled + Few Labels	Combination of Supervised & Unsupervised	Leverage cheap unlabeled data with minimal labeling effort
Reinforcement	No Data (Trial & Error)	Agent, Environment, Rewards, Policy	Learn optimal behavior through rewards and punishments
Stay tuned for the next topics on Machine Learning types!
