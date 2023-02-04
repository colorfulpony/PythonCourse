import pandas

url = "https://docs.google.com/spreadsheets/d/1HG-UBLDX8Efh8g9ze1QiljQIrAU4qYk8_jQSrPz9JSw/gviz/tq?tqx=out:csv&sheet=HUB_20230127_(3781)"
data = pandas.read_csv(url)
print(data)