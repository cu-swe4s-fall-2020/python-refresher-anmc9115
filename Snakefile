STATE = "Colorado"
DATE = "2020-11-24"

rule all:
    input: 'CO_counties_histogram.png', 'CO_countiesdp.png'
   
rule get_daily_rates:
    input: STATE, DATE
    output: 'CO_counites_rates.txt'
    shell: 'python get_daily_rates.py --state Colorado --date 2020-11-24 --output_filename CO_counties'

rule get_deaths_pops:
    input: STATE, DATE
    output: 'CO_countiesdp.txt'
    shell: 'python get_daily_rates.py --state Colorado --date 2020-11-24 --output_filename CO_counties'

rule make_histo:
    input: 'CO_counties_rates.txt'
    output: 'CO_counties_histogram.png'
    shell: 'python ss_plots/histogram.py --in_file CO_counties_rates.txt --out_file CO_counties_histogram.png --x_label "Covid-19 Rates Per Capita in CO Counties 2020-11-24" --y_label "Frequency" --width 3 --height 1'
    
rule make_scatter:
    input: 'CO_countiesdp.txt'
    output: 'CO_countiesdp.png'
    shell: "python ss_plots/scatter.py --in_file CO_countiesdp.txt --out_file CO_countiesdp.png --x_label 'Colorado County Population' --y_label 'Total Deaths'"