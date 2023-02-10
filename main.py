import pandas as pd
import numpy as np
import dateTime


df = pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/athletes.csv')

#print(df['nationality'].value_counts()[:30])

gold = df.groupby('nationality').sum()['gold']
silver = df.groupby('nationality').sum()['silver']
bronze = df.groupby('nationality').sum()['bronze']

total_medals = gold + silver + bronze

#print(total_medals)

now = pd.Timestamp(DT.datetime.now())
df['dob'] = pd.to_datetime(df['dob'])
df['dob'] = df['dob'].where(df['dob'] < now, df['dob'] - np.timedelta64(100, 'Y'))
df['age'] = now - df['dob']).astype('<m8[Y]')
print(df)
          
                            