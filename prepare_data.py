import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime
from dateutil import parser
from datetime import datetime

def read_data():
    incidents = pd.read_csv('data/cleaned_data_no_zeros.csv', sep = None, dtype={'YEAR OCCURRED': np.int_, 'MONTH OCCURRED': np.int_,'GEO CODE': np.str_, 'CRIME CATEGORY DESCRIPTION': np.str_,}, engine = 'python')
    
    length = len(incidents)
    
    # Create columns for onehot_encodings
    onehot_crime_array =  [[]] * length
    onehot_geocode_array =  [[]] * length
    
    # Find Unique Values
    unique_crime_categories = incidents['CRIME CATEGORY DESCRIPTION'].unique()
    unique_geocode = incidents['GEO CODE'].unique()

    # Encode Using np.eye()
    unique_crimes_encoding = np.eye(len(unique_crime_categories))
    unique_geocode_encoding = np.eye(len(unique_geocode))


    # Map Unique Values to Corresponding Encodings 

    crime_dict = {}
    for i in range(len(unique_crime_categories)):
        crime_dict[unique_crime_categories[i]] = unique_crimes_encoding[i]

    geocode_dict = {}
    for i in range(len(unique_geocode)):
        geocode_dict[unique_geocode[i]] = unique_geocode_encoding[i]

    # Iterate through Data Frame to Add Encoded Values to Corresponding Spots

    for i in range(length):
        onehot_crime_array[i] = crime_dict[incidents['CRIME CATEGORY DESCRIPTION'][i]]

    for i in range(length):
        onehot_geocode_array[i] = geocode_dict[incidents['GEO CODE'][i]] 

    # Add Columns to Data Frames

    incidents['CRIME CATEGORY ARRAY'] = onehot_crime_array
    incidents['GEO CODE ARRAY'] = onehot_geocode_array
    
    incidents = incidents.drop(columns=['CRIME CATEGORY DESCRIPTION', 'GEO CODE', 'Unnamed: 0'])
    return incidents
# Get Results:

# incidents.head()