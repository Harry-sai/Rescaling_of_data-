import pandas as pd

read_ds = pd.read_csv('Difference_sorted_a_b.bed',sep='\t',header=None)

read_ds.columns =['Length','Reference_nf','Query_nf','difference']

max_ref = read_ds['Reference_nf'].max()
max_norm_freq_length = read_ds.loc[read_ds["Reference_nf"].idxmax(), "Length"]

read_ds['lines_pull'] = (read_ds['Reference_nf']/max_ref)*max_norm_freq_length

save_ds = read_ds[['Length','lines_pull']]

save_ds.to_csv('Pulling_no_lines.tsv',sep='\t',index=False,header=None)


