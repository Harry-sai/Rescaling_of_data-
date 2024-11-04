import pandas as pd
import matplotlib.pyplot as plt

# Reading the CSV file
final_df = pd.read_csv("Combined_output_with_nf.tsv", sep="\t", header=None)
final_df.columns = ['Length','Refrence_freq','Old_query_nf','differenc','New_query_nf']

# Extracting the columns for plotting
x = final_df['Length']
y1 = final_df['Refrence_freq']       
y2 = final_df['Old_query_nf']       
y3 = final_df['New_query_nf']   

# Plotting the data
plt.plot(x, y1, 'k--', label='Reference')
plt.plot(x, y2, 'r-', label='Query_old')
plt.plot(x, y3, 'y-', label='Query_refined')

# Setting plot titles and labels
plt.title('RESCALING')
plt.xlabel('Length_of_Chromosome')
plt.ylabel('Normalised_Frequency')

# Adding legend and saving the figure
plt.legend(loc=0)
plt.savefig("plot_output.png")  # Save before plt.show()
plt.show()

