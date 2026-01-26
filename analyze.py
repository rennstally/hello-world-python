import pandas as pd

df = pd.read_csv("attention_log.csv")

print("\n--- Attention Stats ---\n")

print("Average attention span (seconds):")
print(df["duration_seconds"].mean())

print("\nTotal switches:")
print(len(df))

print("\nTop windows by total time spent:")
print(df.groupby("window")["duration_seconds"].sum().sort_values(ascending=False))

print("\nMost distracting (short stays):")
print(df.sort_values("duration_seconds").head(10))
