import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# ---------------- Functions ----------------

def load_dataset(filepath):
    """Load dataset from CSV/Excel file (auto-detect sheet)."""
    if filepath.endswith(".csv"):
        df = pd.read_csv(filepath)
    elif filepath.endswith(".xlsx"):
        # load the first sheet automatically
        df = pd.read_excel(filepath, sheet_name=0)
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")
    return df

def label_customers(df):
    """Assign class label based on Payment (Rs)."""
    df['Class'] = ['RICH' if amt > 200 else 'POOR' for amt in df['Payment (Rs)']]
    return df

def prepare_features_targets(df):
    """Prepare features (X) and binary targets (y)."""
    X = df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].values
    y = np.array([1 if lbl == 'RICH' else 0 for lbl in df['Class']])
    return X, y

def train_and_predict(X, y):
    """Train logistic regression and return predictions."""
    clf = LogisticRegression()
    clf.fit(X, y)
    preds = clf.predict(X)
    return clf, preds

def evaluate_model(y_true, y_pred):
    """Generate classification report and accuracy."""
    report = classification_report(y_true, y_pred, target_names=['POOR', 'RICH'])
    acc = accuracy_score(y_true, y_pred)
    return report, acc

def add_predictions(df, preds):
    """Add model predictions to dataframe."""
    df['Prediction'] = ['RICH' if p == 1 else 'POOR' for p in preds]
    return df

# ---------------- Main Program ----------------

if __name__ == "__main__":
    filepath = "Lab Session Data (1).xlsx"   # <---- put your file path here

    # Step 1: Load dataset
    df = load_dataset(filepath)

    # Step 2: Label customers
    df = label_customers(df)

    # Step 3: Prepare features and targets
    X, y = prepare_features_targets(df)

    # Step 4: Train model and predict
    clf, preds = train_and_predict(X, y)

    # Step 5: Evaluate model
    report, acc = evaluate_model(y, preds)

    # Step 6: Add predictions to DataFrame
    df = add_predictions(df, preds)

    # -------- Results --------
    print("Classification Report")
    print(report)
    print(f"Accuracy: {acc:.2f}\n")

    print("Customer Classification")
    print(df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)', 'Payment (Rs)', 'Class', 'Prediction']])
