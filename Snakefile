STATE = "Colorado"
DATE = "2020-11-24"

rule all:
    input: 'CO_counties_hist.png'
   
rule get_daily_rates:
    input: STATE, DATE
    output: 'CO_counites_rates.txt'
    shell: 'python get_daily_rates.py --state Colorado --date 2020-08-09 --output_filename CO_counties'

rule make_histo:
    input: 'CO_counties_rates.txt'
    output: 'CO_counties_hist.png'
    shell: 'python ss_plots/histogram.py --in_file CO_counties_rates.txt --out_file CO_counties_histogram.png --x_label "Covid-19 Rates Per Capita in CO Counties 2020-11-24" --y_label "Frequency" --width 3 --height 1'