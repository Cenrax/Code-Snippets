import pandas as pd

def load_data(path,datasetName):
  return pd.read_csv(os.path.join(path,datasetName))
