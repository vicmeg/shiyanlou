import json
import pandas as pd

def analysis(file, user_id):

    try:
        df = pd.read_json(file)
    except ValueError:
        return 0, 0

    s = df[df['user_id'] == user_id].minutes
    return s.count(), s.sum()
