#A4
import statistics
import numpy as np

# ---- Hardcoded Data (sample of thyroid dataset) ----
data = [
    {"age": 35, "sex": "F", "on_thyroxine": "f", "TSH": 0.005, "T3": 2.0, "TT4": 120, "T4U": 1.2, "FTI": 100, "TBG": 25, "Class": "normal"},
    {"age": 52, "sex": "M", "on_thyroxine": "t", "TSH": 530.0, "T3": 0.9, "TT4": 200, "T4U": 2.0, "FTI": 881, "TBG": 180, "Class": "abnormal"},
    {"age": 42, "sex": "F", "on_thyroxine": "f", "TSH": 1.5, "T3": 2.5, "TT4": 150, "T4U": 0.8, "FTI": 120, "TBG": 40, "Class": "normal"},
    {"age": 70, "sex": "F", "on_thyroxine": "f", "TSH": 0.02, "T3": 1.0, "TT4": 90,  "T4U": 1.0, "FTI": 85,  "TBG": 30, "Class": "normal"},
    {"age": 30, "sex": "?", "on_thyroxine": "f", "TSH": "?",   "T3": "?",  "TT4": 140, "T4U": 0.9, "FTI": 110, "TBG": "?", "Class": "abnormal"},
]

# ---- 1. Data Type Identification ----
print("---- Data Type Identification ----")
print("Numeric attributes     : age, TSH, T3, TT4, T4U, FTI, TBG")
print("Categorical attributes : sex, on_thyroxine, Class")
print("Encoding suggestion    : One-Hot Encoding for all categoricals\n")

# ---- 2. Missing Value Detection ----
missing_counts = {}
for key in data[0]:
    missing_counts[key] = sum(1 for row in data if row[key] == '?')
print("---- Missing Values per Attribute ----")
for k, v in missing_counts.items():
    if v > 0:
        print(f"{k}: {v}")
print()

# ---- 3. Replace missing values with most frequent ----
def most_frequent(values):
    return max(set(values), key=values.count)

# Replace '?' with mode for each column
columns = data[0].keys()
for col in columns:
    col_values = [row[col] for row in data if row[col] != '?']
    if all(isinstance(val, (int, float)) for val in col_values):
        # Convert all to float
        col_values = list(map(float, col_values))
        fill_value = round(statistics.mean(col_values), 2)
    else:
        fill_value = most_frequent(col_values)
    for row in data:
        if row[col] == '?':
            row[col] = fill_value

# ---- 4. Outlier Detection (using IQR method) ----
def count_outliers(values):
    Q1 = np.percentile(values, 25)
    Q3 = np.percentile(values, 75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return sum(1 for v in values if v < lower or v > upper)

print("---- Outlier Detection ----")
numeric_keys = ["age", "TSH", "T3", "TT4", "T4U", "FTI", "TBG"]
for key in numeric_keys:
    vals = [float(row[key]) for row in data]
    print(f"{key}: {count_outliers(vals)} outliers")

# ---- 5. Mean and Std Dev for numeric columns ----
print("\n---- Mean and Std Dev ----")
for key in numeric_keys:
    vals = [float(row[key]) for row in data]
    mean_val = round(statistics.mean(vals), 2)
    std_val = round(statistics.stdev(vals), 2)
    print(f"{key} - Mean: {mean_val}, Std Dev: {std_val}")