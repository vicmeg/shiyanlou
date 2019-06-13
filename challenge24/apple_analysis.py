import pandas as pd

def quarter_volume():

    data = pd.read_csv('apple.csv',header=0)

    e = data.Volume
    e.index = pd.to_datetime(data.Date)

    second_volume = e.resample('Q').sum().sort_values()[-2]

    return second_volume
