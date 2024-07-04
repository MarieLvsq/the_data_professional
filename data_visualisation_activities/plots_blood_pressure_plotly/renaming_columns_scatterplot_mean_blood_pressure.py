import pandas as pd
import plotly.express as px

# Load the CSV file into a DataFrame
file_path = '2_bloodpressure_plotly.csv'
blood_pressure_data = pd.read_csv(file_path)

# Rename the columns
blood_pressure_data.rename(columns={
    'Country/Region/World': 'Country',
    'ISO': 'ISO_Code',
    'Mean systolic blood pressure (mmHg)': 'SBP',
    'Mean diastolic blood pressure (mmHg)': 'DBP'
}, inplace=True)

#Drop columns
blood_pressure_data.drop(columns=['Sex', 'Year', 'Prevalence of raised blood pressure'], inplace=True)

# Create the animated scatter plot
fig = px.scatter(blood_pressure_data, 
                 x="SBP", 
                 y="DBP", 
                 hover_name="Country",  
                 range_x=[blood_pressure_data["SBP"].min(), blood_pressure_data["SBP"].max()],
                 range_y=[blood_pressure_data["DBP"].min(), blood_pressure_data["DBP"].max()],
                 title="Blood Pressure Distribution",
                 labels={"SBP": "Systolic Blood Pressure", 
                         "DBP": "Diastolic Blood Pressure"})

fig.show()

# Rename the columns
blood_pressure_data.rename(columns={
    'Country/Region/World': 'Country',
    'ISO': 'ISO_Code',
    'Mean systolic blood pressure (mmHg)': 'SBP',
    'Mean diastolic blood pressure (mmHg)': 'DBP'
}, inplace=True)

