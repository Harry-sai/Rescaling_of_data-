In the Snakemake file `Run.smk`, I have created six rules, including the `rule all`, which coordinates the production of the desired outputs in a sequential manner. The `rule all` encompasses all outputs from the various rules, except for the `Subsampling` rule, which we need to force run.

1. **First Rule**: `all` - This rule collects all the outputs from the different rules, excluding the `Subsampling` rule.

2. **Second Rule**: `Normalise_freq_shuf_ab_file` - This rule generates two files: a difference file containing four columns (length, reference Nf, query Nf, and the difference) and a combined BED file of `shuf.a` and `shuf.b`, which is utilized in the `Subsampling` rule. I created a script named `new_cal.sh` to handle this process.

3. **Third Rule**: `Pulling` - This rule calculates the number of lines to be pulled from the combined BED file for subsampling, using the `Calculation.py` script.

4. **Fourth Rule**: `Subsampling` - In this rule, we read from `pulling_no_lines.tsv` to extract the specified number of lines from `combined_ab.bed`. For this, I wrote a Python script called `Subsample_code.py`. This rule allows for the specification of multiple shuffled files by adjusting the `NUM_OF_FILES` section in Snakemake.

5. **Fifth Rule**: `Finding Nf` - Here, I calculate the Nf of the new file, knowing that the number of pulled lines corresponds to the frequency of the new BED file. This is done using the `pulling_no_lines.tsv` file, and I implemented this logic in the script `subsampled_nf.py`.

6. **Last Rule**: `Plotting` - This rule generates a rescaled plot from the data in `Combined_output_with_nf.tsv`, using Matplotlib in the `plotting.py` script.

To run the workflow, first activate the Snakemake environment with:
```
conda activate snakemake_env
```
Then execute the following command to run Snakemake while forcing the execution of the `Subsampling` rule:
```
snakemake --cores 2 --snakefile Run.smk --forcerun Subsampling
```
