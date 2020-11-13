import pandas

csv_data = pandas.read_csv('country_wise_latest'.csv)
print(csv_data[1][1])