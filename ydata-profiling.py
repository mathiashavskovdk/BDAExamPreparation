# Installing library
pip install ydata-profiling

# Importing libraries
from ydata_profiling import ProfileReport
import pandas as pd

# Loading dataset
df = pd.read_pickle('Datasets/flight_dataset_sample_small.pkl')

# Generating report (remember to change title)
profile = ProfileReport(df, title='Flight Dataset')
profile.to_file('example.html')

# If you have a very large dataset you can either take a stratified sample or use the minimal=True
# profile = ProfileReport(df, title="Flight Dataset", minimal=True)

# Be aware that the script generates a HTML file (a local website) in the same folder as the code. You need to open this file to see the result.
