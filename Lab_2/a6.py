#A6
C1 = [20, 6, 2, 386]
C2 = [16, 3, 6, 289]
# Compute dot product
dot = 0
for i in range(len(C1)):
    dot += C1[i] * C2[i]

# Compute magnitudes
mag_C1 = sum([x*x for x in C1]) ** 0.5
mag_C2 = sum([x*x for x in C2]) ** 0.5

# Compute cosine similarity
cos_sim = dot / (mag_C1 * mag_C2) if mag_C1 != 0 and mag_C2 != 0 else 0

# Output
print("Version 1: Raw Vectors")
print("Cosine Similarity:", round(cos_sim, 4))