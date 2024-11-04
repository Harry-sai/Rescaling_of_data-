import pandas as pd
import numpy as np

difference_df = pd.read_csv("Difference_sorted_a_b.bed", sep='\t', header=None)
difference_df.columns = ["Length", "NF_Ref","NF_old_q","Difference"]


pulling_df = pd.read_csv("Pulling_no_lines.tsv", sep='\t', header=None)
pulling_df.columns = ["Length", "Frequency"]
pulling_df["Frequency"] = np.ceil(pulling_df["Frequency"]).astype(int)


total = pulling_df["Frequency"].sum()
print(total)
pulling_df["Normalized_Frequency"] = pulling_df["Frequency"] / total


combined_df = difference_df.copy()
combined_df["Normalized_Frequency"] = pulling_df["Normalized_Frequency"]

# Save combined content to a new file without affecting the original Difference_sorted_a_b.bed
combined_df.to_csv("Combined_output_with_nf.tsv", sep='\t', index=False,header=False)
