#Steps
#read csv directly from johns hopkins
#group entire csv according to countries ; get rid of provinces
#make sure taiwan is renamed to prevent potential injection errors into sql
#drop lat and long, we can add them in later during analysis
#transpose the dataframe so that the new entries can be added via rows, rather than adding a column to the database everyday
#filter out latest date
#connect to database
#load dataframe into database
#close connection

import pandas as pd
import sqlalchemy
import datetime

##Total Confirmed Cases###############################################################################################################
url_case = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
df_cases = pd.read_csv(url_case)
df_cases = df_cases.groupby(['Country/Region']).sum().reset_index()
df_cases.loc[df_cases['Country/Region']=='Taiwan*', 'Country/Region'] = 'Taiwan'
df_cases_final = df_cases.drop(columns = ['Lat','Long']).set_index('Country/Region').transpose()
df_cases_final = df_cases_final.reset_index()
df_cases_final.rename(columns = {'index': 'Date'}, inplace = True)
df_cases_final['Date'] = pd.to_datetime(df_cases_final['Date'])


##Total Deaths######################################################################################################################
url_death = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
df_death = pd.read_csv(url_death)
df_death = df_death.groupby(['Country/Region']).sum().reset_index()
df_death.loc[df_death['Country/Region'] == 'Taiwan*', 'Country/Region'] = 'Taiwan'
df_death_final = df_death.drop(columns = ['Lat','Long']).set_index('Country/Region').transpose()
df_death_final = df_death_final.reset_index()
df_death_final.rename(columns = {'index': 'Date'}, inplace = True)
df_death_final['Date'] = pd.to_datetime(df_death_final['Date'])


##Total Recovery####################################################################################################################
url_recov = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
df_recov = pd.read_csv(url_recov)
df_recov = df_recov.groupby(['Country/Region']).sum().reset_index()
df_recov.loc[df_recov['Country/Region'] == 'Taiwan*', 'Country/Region'] = 'Taiwan'
df_recov_final = df_recov.drop(columns = ['Lat','Long']).set_index('Country/Region').transpose()
df_recov_final = df_recov_final.reset_index()
df_recov_final.rename(columns = {'index': 'Date'}, inplace = True)
df_recov_final['Date'] = pd.to_datetime(df_recov_final['Date'])

## Connection to Database and load data in##########################################################################################
db_url = 'mysql+pymysql://root:password@localhost:3306/'+'covid'+'?charset=utf8'
db_connection = sqlalchemy.create_engine(db_url)

condition_cases = df_cases_final['Date'] == datetime.date.today().strftime("%Y/%m/%d")
condition_death = df_death_final['Date'] == datetime.date.today().strftime("%Y/%m/%d")
condition_recov = df_recov_final['Date'] == datetime.date.today().strftime("%Y/%m/%d")

df_cases_daily = df_cases_final[condition_cases]
df_death_daily = df_death_final[condition_death]
df_recov_daily = df_recov_final[condition_recov]

df_cases_daily.to_sql('Total_Confirmed_Cases', db_connection, if_exists = 'append', index = False)
df_death_daily.to_sql('Total_Deaths', db_connection, if_exists = 'append', index = False)
df_recov_daily.to_sql('Total_Recoveries', db_connection, if_exists = 'append', index = False)

db_connection.dispose()