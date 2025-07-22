#A5
import numpy as np

# Binary Vectors for Jaccard & SMC
A = np.array([1, 0, 1, 1, 0, 1])
B = np.array([1, 1, 1, 0, 0, 1])

# --- Jaccard Similarity ---
intersection = np.sum((A & B))
union = np.sum((A | B))
jaccard = intersection / union

# --- Simple Matching Coefficient (SMC) ---
matches = np.sum(A == B)
smc = matches / len(A)

print("---- Binary Similarity ----")
print(f"Jaccard Similarity      : {jaccard:.2f}")
print(f"Simple Matching Coef.   : {smc:.2f}")

# A5
C1 = [20, 6, 2, 386]
C2 = [16, 3, 6, 289]

# Fixed thresholds for binarization
thresholds = [18, 4, 3, 300]  # chosen manually based on general range

binary_C1 = []
binary_C2 = []

for i in range(len(C1)):
    binary_C1.append(1 if C1[i] > thresholds[i] else 0)
    binary_C2.append(1 if C2[i] > thresholds[i] else 0)

# Compare binary vectors
f11 = f10 = f01 = f00 = 0
for i in range(len(binary_C1)):
    if binary_C1[i] == 1 and binary_C2[i] == 1:
        f11 += 1
    elif binary_C1[i] == 1 and binary_C2[i] == 0:
        f10 += 1
    elif binary_C1[i] == 0 and binary_C2[i] == 1:
        f01 += 1
    else:
        f00 += 1

jc = f11 / (f11 + f10 + f01) if (f11 + f10 + f01) else 0
smc = (f11 + f00) / (f11 + f10 + f01 + f00) if (f11 + f10 + f01 + f00) else 0

print("Binary C1:", binary_C1)
print("Binary C2:", binary_C2)
print("JC:", round(jc, 4), "SMC:", round(smc, 4))