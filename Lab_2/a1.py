import pandas as pd
import numpy as np

# ------------------ Functions ------------------

def find_purchase_sheet(file_path):
    """
    Finds the sheet name that contains 'Purchase' (case-insensitive).
    Returns the first matching sheet name.
    """
    xls = pd.ExcelFile(file_path)
    for sheet in xls.sheet_names:
        if "purchase" in sheet.lower():
            return sheet
    raise ValueError("No sheet containing 'Purchase' found in the file.")

def load_purchase_data(file_path):
    """
    Load Purchase Data sheet and segregate into:
    A = product quantities matrix
    C = payment vector
    """
    sheet_name = find_purchase_sheet(file_path)   # find correct sheet
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Feature matrix A (Candies, Mangoes, Milk Packets)
    A = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]].values

    # Target vector C (Payments)
    C = df["Payment (Rs)"].values
    return A, C

def get_vector_space_info(A):
    """
    Compute vector space properties:
    - Dimensionality
    - Number of vectors
    - Rank of A
    """
    dimensionality = A.shape[1]
    num_vectors = A.shape[0]
    rank = np.linalg.matrix_rank(A)
    return dimensionality, num_vectors, rank

def compute_product_costs(A, C):
    """
    Estimate product costs using pseudo-inverse:
    Solves AX = C
    """
    A_pinv = np.linalg.pinv(A)
    X = A_pinv @ C
    return X

# ------------------ Main Program ------------------

if __name__ == "__main__":
    file_path = "Lab Session Data (1).xlsx"

    # Load data safely
    A, C = load_purchase_data(file_path)

    # Vector space properties
    dimensionality, num_vectors, rank = get_vector_space_info(A)

    # Solve for costs
    product_costs = compute_product_costs(A, C)

    # Results
    print("Dimensionality of vector space:", dimensionality)
    print("Number of vectors in this space:", num_vectors)
    print("Rank of Matrix A:", rank)

    print("\nEstimated Cost per Product:")
    print("Candies (Rs per unit):", round(product_costs[0], 2))
    print("Mangoes (Rs per Kg):", round(product_costs[1], 2))
    print("Milk Packets (Rs per unit):", round(product_costs[2], 2))
