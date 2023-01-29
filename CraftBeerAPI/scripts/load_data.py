from django.apps import apps
import pandas as pd

def run():
    print('reading csv ...')
    df = pd.read_csv('assets/beer_output.csv')

    print(df)

if __name__ == "__main__":
    run()



# import data from CSV file:
# csv_list1 = beer.import_data(data = open('beer_output.csv'))
# import data from CSV file with pandas:
# df = pd.read_csv('beer_output.csv')
# csv_list2 = beer.import_data(df)
# first_row = csv_list2[0]