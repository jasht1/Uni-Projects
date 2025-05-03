import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.linear_model import LogisticRegression

def evaluate_predictive_power(df, measure_col="Young's Modulus [Pa]", group_col="Group"):
    # Convert group labels to binary
    group_labels = df[group_col].unique()
    assert len(group_labels) == 2, "Only supports binary groups"
    df = df.copy()
    df["GroupBinary"] = (df[group_col] == group_labels[1]).astype(int)
    
    X = df[[measure_col]].values
    y = df["GroupBinary"].values

    # AUC
    auc = roc_auc_score(y, df[measure_col])

    # Logistic Regression
    model = LogisticRegression()
    model.fit(X, y)
    logreg_acc = model.score(X, y)
    coef = model.coef_[0][0]

    # Effect size (Cohen's d)
    group1 = df[df["GroupBinary"] == 0][measure_col]
    group2 = df[df["GroupBinary"] == 1][measure_col]
    pooled_std = np.sqrt(((group1.std() ** 2) + (group2.std() ** 2)) / 2)
    cohen_d = (group2.mean() - group1.mean()) / pooled_std

    # Naive threshold accuracy
    threshold = df[measure_col].median()
    preds = (df[measure_col] > threshold).astype(int)
    naive_acc = accuracy_score(y, preds)

    return {
        "AUC": auc,
        "LogReg Accuracy": logreg_acc,
        "LogReg Coef": coef,
        "Cohen's d": cohen_d,
        "Median Threshold Accuracy": naive_acc
    }

def combined_data ():
  from import_data import get_jpk_batch_data as get_jpk_batch_data
  batch_data = get_jpk_batch_data()

  data_sets = []
  for group in batch_data:
    batch_data[group].insert(1, "Group" ,[group]* len(batch_data[group]))
    data_sets.append(batch_data[group][["Group", "Filename", "Young's Modulus [Pa]", "ResidualRMS [N]"]])

  combined_data = pd.concat(data_sets, ignore_index=True)

  return combined_data

# metrics = evaluate_predictive_power(combined_data())
# print(metrics)
