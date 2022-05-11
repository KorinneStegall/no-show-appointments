# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:01:31 2022

@author: korin
"""

#packages
import pandas as pd

#dataset
df = pd.read_csv("C:/Users/korin/OneDrive/Documents/GitHub/no_show_proj/no_show_may_2016.csv")

#cleaning:
#df.info()

#renaming columns
df = df.rename(columns = {'No-show':'no_show', 'ScheduledDay':'scheduled_day',
                          'AppointmentDay':'appointment_day', 'Hipertension':'hypertension',
                          'Handcap':'handicap'})
#dropping columns
df.drop('PatientId', axis=1, inplace=True)
df.drop('AppointmentID', axis=1, inplace=True)

#changing all to lowercase
df.rename(columns = lambda x: x.strip().lower(), inplace=True)

#changing datatypes
#bools
boo_columns = df.iloc[:, 5:11]
for c in boo_columns:
    df[c] = df[c].astype(bool)
    
def noshow_to_boolean(status):
    '''Changing strings in the no show column to bools'''
    if status == 'No':
        return False
    else:
        return True
df["no_show"] = df["no_show"].apply(noshow_to_boolean)

#datetime
df['scheduled_day'] = pd.to_datetime(df['scheduled_day'])
df['appointment_day'] = pd.to_datetime(df['appointment_day'])

df.to_csv('no_show.csv', index = False)
test = pd.read_csv('no_show.csv')
