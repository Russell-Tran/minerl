import pandas as pd 

shit = []
for i in range(100):
	shit.append({
		"taco" : "this is taco number {}".format(i),
		"mesa" : "this is mesa number {}".format(i)

		})

df = pd.DataFrame(shit)

df.to_csv("shit_practice.csv")