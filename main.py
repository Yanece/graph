import pandas

csv_content = pandas.read_csv("parcours_explorateurs.csv")
print(csv_content.head(100))
