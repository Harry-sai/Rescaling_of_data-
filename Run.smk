rule all:
    input:
        expand("Difference_sorted_{x}_{y}.bed", x=["a"], y=["b"]),
        "Pulling_no_lines.tsv",
        "Combined_output_with_nf.tsv",
        "plot_output.png"
        
        
rule Normalise_freq_shuf_ab_file:
    input:
        a = "shuf.{x}.bed.gz",  
        b = "shuf.{y}.bed.gz"   
    output:
        "Difference_sorted_{x}_{y}.bed",  
        combined = "combined_{x}{y}.bed",
          
    shell:
        "./new_cal.sh {input.a} {input.b} {output[0]} {output.combined}"


rule Pulling:
    input:
        "Difference_sorted_a_b.bed"
    output:
        "Pulling_no_lines.tsv"
    shell:
        "python3 Calculation.py"

NUM_OF_FILES = 5
rule Subsampling:
    input:
        a = "combined_ab.bed",
        b = "Pulling_no_lines.tsv"
    output:
        expand("shuffled_output_{index}.bed",index=range(1, NUM_OF_FILES + 1))
    params:
        num_files = NUM_OF_FILES
    shell:
        "python3 Subsample_code.py {input.a} {input.b} shuffled_output {params.num_files}"
    

rule Calculation_nf_new:
    input:
        A = "Pulling_no_lines.tsv",
        B = "Difference_sorted_a_b.bed"
    output:
        "Combined_output_with_nf.tsv"
    shell:
        "python3 subsampled_nf.py"
    

rule Plotting:
    input:
        "Combined_output_with_nf.tsv"
    output:
        "plot_output.png"
    shell:
        "python3 plotting.py"
