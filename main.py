from logging import root
import pandas

csv_content = pandas.read_csv("parcours_explorateurs.csv")
print(csv_content.head(100))

adjacent_table = {}
adjacent_table = {
    row["noeud_amont"]: row["noeud_aval"] for _, row in csv_content.iterrows()
}
