from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Mehmet", "Hayvan"])
table.align = "l"

print(table)
