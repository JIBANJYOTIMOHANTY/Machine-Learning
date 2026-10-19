# Financial Fraud Detection with Cost-Sensitive Machine Learning

An end-to-end Machine Learning pipeline implemented in Jupyter Notebook ([Fraud_Detection.ipynb](file:///Users/jibanjyotimohanty/Jiban%20Drive/Machine-Learning/project/Fraud%20Detection/Fraud_Detection.ipynb)) to detect fraudulent transactions under extreme class imbalance using cost-sensitive threshold optimization.

---

## 📌 Project Overview

Fraud detection is a classic **imbalanced classification** problem where fraudulent transactions are extremely rare compared to legitimate ones (~5% of all transactions). Traditional accuracy-based metrics fail in this domain because a naive model predicting "non-fraud" all the time would achieve 95% accuracy while missing 100% of fraud cases.

This project tackles fraud detection by:
1. Handling class imbalance using balanced class weighting (`class_weight="balanced"`).
2. Comparing **Logistic Regression** and **Random Forest Classifier**.
3. Applying **cost-sensitive threshold tuning** based on domain-specific financial penalties:
   - **Cost of a Missed Fraud (False Negative - FN):** ₹5,000
   - **Cost of a False Alarm (False Positive - FP):** ₹200
4. Evaluating models on **PR-AUC (Precision-Recall Area Under Curve)**, **Precision**, **Recall**, and **Total Business Cost**.

---

## 🏗️ Architecture & Workflow

```mermaid
flowchart TD
    A[Synthetic Data Generation\n1,000 Samples, 6 Features, 5.4% Fraud] --> B[Data Splitting\n60% Train | 20% Val | 20% Test]
    B --> C[Feature Scaling\nStandardScaler]
    C --> D[Model Training\nBalanced Class Weights]
    D --> E1[Logistic Regression]
    D --> E2[Random Forest Classifier]
    E1 --> F[Cost-Sensitive Threshold Search\nThresholds: 0.05 to 0.95]
    E2 --> F
    F --> G[Validation Model Comparison\nPR-AUC & Min Cost ₹]
    G --> H[Final Test Set Evaluation\nBusiness Cost & Confusion Matrix]
```

---

## 📊 Dataset Details

The dataset is synthetically generated using Scikit-Learn's `make_classification` to simulate typical banking transactions:

| Property | Value | Description |
| :--- | :--- | :--- |
| **Total Samples** | 1,000 | Total transactions generated |
| **Features** | 6 (`Feature_1` to `Feature_6`) | 4 informative, 1 redundant, 1 repeated |
| **Class Distribution** | 946 Legitimate (94.6%) vs. 54 Fraud (5.4%) | Highly skewed / imbalanced |
| **Class Separation** | 1.0 | Degree of separation between clusters |
| **Label Noise (`flip_y`)**| 0.01 | 1% noise introduced to simulate real-world errors |

### Data Splitting Strategy
- **Train Set (60%)**: 600 transactions
- **Validation Set (20%)**: 200 transactions (Stratified split)
- **Test Set (20%)**: 200 transactions (Stratified split)

---

## ⚙️ Models & Preprocessing

1. **Preprocessing**:
   - `StandardScaler`: Fitted exclusively on the training set and applied to validation and test sets to prevent data leakage.
2. **Algorithms**:
   - **Logistic Regression**: Baseline linear classifier with `class_weight='balanced'` and `max_iter=1000`.
   - **Random Forest**: Non-linear ensemble model with `n_estimators=200`, `min_samples_leaf=2`, and `class_weight='balanced'`.

---

## 💰 Cost Matrix & Threshold Tuning

In real-world fraud operations, **False Negatives** (letting a fraudster escape with money) cost significantly more than **False Positives** (customer inconvenience of sending an OTP / alert).

$$\text{Total Business Cost} = (FN \times \text{MISSED\_FRAUD\_COST}) + (FP \times \text{FALSE\_ALARM\_COST})$$

- $\text{MISSED\_FRAUD\_COST} = ₹5,000$
- $\text{FALSE\_ALARM\_COST} = ₹200$

Instead of using a default probability threshold of `0.50`, thresholds from `0.05` to `0.95` are evaluated on the validation set to find the threshold that minimizes total monetary loss.

---

## 📈 Results & Findings

### Validation Set Performance

| Model | Precision @ 0.50 | Recall @ 0.50 | F1 @ 0.50 | PR-AUC | Optimal Threshold | Minimum Validation Cost (₹) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** | 0.094 | 0.462 | 0.156 | 0.229 | 0.06 | ₹36,200 |
| **Random Forest** ⭐ | **0.750** | **0.462** | **0.571** | **0.601** | **0.17** | **₹19,200** |

> **Conclusion**: **Random Forest** substantially outperformed Logistic Regression across all metrics (PR-AUC of 0.601 vs 0.229) and achieved nearly half the business error cost (₹19,200 vs ₹36,200).

---

## ⚠️ Important Implementation Note (Notebook Fix)

In cell 10 of `Fraud_Detection.ipynb`, when saving the optimal threshold:

```python
# In Cell 10, line 311:
best_threshold = threshold  # ⚠️ Bug: overwrites with the last loop item (0.95)
```

Because `threshold` is the loop iterator that terminates at `0.95`, `best_threshold` was inadvertently set to `0.95` instead of `model_best_threshold` (`0.17`). At threshold `0.95`, the model fails to detect any test fraud cases.

### Recommended Fix:
Change line 311 in cell 10 to:
```python
best_threshold = model_best_threshold  # Sets the optimal threshold (0.17 for Random Forest)
```

With `best_threshold = 0.17`, the model correctly catches fraudulent test cases at minimal business cost.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Jupyter Notebook or VS Code / IDE with Jupyter extension

### Dependencies

Install the required Python packages:

```bash
pip install numpy pandas scikit-learn
```

### Running the Notebook

1. Launch your Jupyter environment or open the folder in your IDE.
2. Open [`Fraud_Detection.ipynb`](file:///Users/jibanjyotimohanty/Jiban%20Drive/Machine-Learning/project/Fraud%20Detection/Fraud_Detection.ipynb).
3. Select your Python kernel/virtual environment.
4. Run all cells sequentially (`Run All`).

---

## 📁 Project Structure

```text
Fraud Detection/
├── Fraud_Detection.ipynb    # Main Jupyter Notebook with data pipeline & modeling
└── README.md                # Project documentation and analysis
```
