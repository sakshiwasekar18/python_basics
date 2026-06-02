# =============================
# PANDAS NULL HANDLING FULL PRACTICE FILE
# =============================

import pandas as pd

# -----------------------------
# 1. LOAD DATA
# -----------------------------
df = pd.read_csv("data.csv")
print("\nOriginal Data:\n", df)

# -----------------------------
# 2. CHECK NULL VALUES
# -----------------------------
print("\nCheck null (True/False):\n", df.isnull())

# Count null values in each column
print("\nNull count per column:\n", df.isnull().sum())

# -----------------------------
# 3. CHECK NULL IN SPECIFIC COLUMN
# -----------------------------
print("\nNull in marks column:\n", df["marks"].isnull())
print("\nCount null in marks:", df["marks"].isnull().sum())

# -----------------------------
# 4. FILTER ROWS WITH NULL VALUES
# -----------------------------
print("\nRows where marks is NULL:\n", df[df["marks"].isnull()])

# -----------------------------
# 5. FILL NULL VALUES
# -----------------------------

# Fill all null with 0
df_fill_all = df.copy()
df_fill_all.fillna(0, inplace=True)
print("\nFill all null with 0:\n", df_fill_all)

# Fill specific column (marks)
df_fill_marks = df.copy()
df_fill_marks["marks"].fillna(50, inplace=True)
print("\nFill marks with 50:\n", df_fill_marks)

# Fill with mean (best practice)
df_fill_mean = df.copy()
df_fill_mean["marks"].fillna(df_fill_mean["marks"].mean(), inplace=True)
print("\nFill marks with mean:\n", df_fill_mean)

# Fill text column
df_fill_city = df.copy()
df_fill_city["city"].fillna("Unknown", inplace=True)
print("\nFill city with 'Unknown':\n", df_fill_city)

# -----------------------------
# 6. DROP NULL VALUES
# -----------------------------

# Drop rows with any null
df_drop_all = df.copy()
df_drop_all.dropna(inplace=True)
print("\nDrop rows with any null:\n", df_drop_all)

# Drop rows where specific column is null
df_drop_marks = df.copy()
df_drop_marks.dropna(subset=["marks"], inplace=True)
print("\nDrop rows where marks is null:\n", df_drop_marks)

# Drop columns with null values
df_drop_cols = df.copy()
df_drop_cols.dropna(axis=1, inplace=True)
print("\nDrop columns with null:\n", df_drop_cols)

# -----------------------------
# 7. THRESHOLD (IMPORTANT)
# -----------------------------

# Keep rows with at least 2 non-null values
df_thresh = df.copy()
df_thresh.dropna(thresh=2, inplace=True)
print("\nKeep rows with at least 2 non-null values:\n", df_thresh)

# -----------------------------
# 8. FORWARD FILL / BACKWARD FILL
# -----------------------------

df_ffill = df.copy()
df_ffill.fillna(method="ffill", inplace=True)
print("\nForward fill:\n", df_ffill)


df_bfill = df.copy()
df_bfill.fillna(method="bfill", inplace=True)
print("\nBackward fill:\n", df_bfill)

# -----------------------------
# 9. CHECK NOT NULL
# -----------------------------
print("\nNot null values in marks:\n", df["marks"].notnull())

# -----------------------------
# 10. FINAL CLEANING EXAMPLE (REAL TASK)
# -----------------------------

clean_df = df.copy()

# Remove rows with no name
clean_df.dropna(subset=["name"], inplace=True)

# Fill marks with mean
clean_df["marks"].fillna(clean_df["marks"].mean(), inplace=True)

# Fill city with 'Unknown'
clean_df["city"].fillna("Unknown", inplace=True)

# Drop rows where age is missing
clean_df.dropna(subset=["age"], inplace=True)

print("\nFinal Cleaned Data:\n", clean_df)

# =============================
# END OF FILE
# =============================
