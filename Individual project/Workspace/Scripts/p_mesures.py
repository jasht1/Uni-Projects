import pandas as pd
import numpy as np

def evaluate_predictive_power(df, measure_col="Young's Modulus [Pa]", group_col="Group"):
  from sklearn.metrics import roc_auc_score, accuracy_score
  from sklearn.linear_model import LogisticRegression
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


def corr_groupVym():
  from import_data import get_jpk_combined_data
  metrics = evaluate_predictive_power(get_jpk_combined_data())
  print(metrics)

def corr_rangeVym ():
  from import_data import get_results_data
  from matplotlib import pyplot as plt
  plt.figure(figsize=(6,4))
  data = get_results_data()

  colors = {'Control': 'blue', 'Treated': 'red'}
  for group in data["Group"].unique():
    group_data=data[data["Group"]==group]
    range = group_data["Max Young's Modulus [Pa]"] - group_data["Min Young's Modulus [Pa]"]
    ym = group_data["Young's Modulus [Pa]"]
    plt.scatter(ym,range,c=colors[group],alpha=0.3)
    m,c = np.polyfit(ym,range,1)
    plt.plot(ym,m*ym+c,label=f"{group} Group Trend",c=colors[group],alpha=0.5)

  range = data["Max Young's Modulus [Pa]"] - data["Min Young's Modulus [Pa]"]
  ym = data["Young's Modulus [Pa]"]
  m,c = np.polyfit(ym,range,1)
  plt.plot(ym,m*ym+c, label="General Trend",alpha=0.5,linewidth=2.5)

  plt.legend()
  plt.xlabel("Apparent Cell Young's Modulus [Pa]")
  plt.ylabel("Range in Young's Modulus Acrros Tests [Pa]")
  plt.tight_layout()
  plt.show()

corr_rangeVym()

