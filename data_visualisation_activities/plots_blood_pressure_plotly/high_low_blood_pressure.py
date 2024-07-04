import pandas as pd
import plotly.express as px

file_path = '2_bloodpressure_plotly.csv'
blood_pressure_data = pd.read_csv(file_path)

blood_pressure_data.rename(columns={
    'Country/Region/World': 'Country',
    'ISO': 'ISO_Code',
    'Mean systolic blood pressure (mmHg)': 'SBP',
    'Mean diastolic blood pressure (mmHg)': 'DBP'
}, inplace=True)

blood_pressure_data.drop(columns=['Sex', 'Year', 'Prevalence of raised blood pressure'], inplace=True)

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

blood_pressure_data.rename(columns={
    'Country/Region/World': 'Country',
    'ISO': 'ISO_Code',
    'Mean systolic blood pressure (mmHg)': 'SBP',
    'Mean diastolic blood pressure (mmHg)': 'DBP'
}, inplace=True)

# Create a new column with high (>= 130) and low SBP class
blood_pressure_data['SBP_Class'] = blood_pressure_data['SBP'].apply(lambda x: 'high' if x >= 130 else 'low')

# Create a choropleth map of world SBP
fig = px.choropleth(blood_pressure_data, 
                    locations="ISO_Code", 
                    color="SBP", 
                    hover_name="Country", 
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="World SBP Distribution")

# Show the plot for world SBP distribution
fig.show()

# Map countries with high SBP only
high_sbp = blood_pressure_data[blood_pressure_data['SBP_Class'] == 'high']

fig_high_sbp = px.choropleth(high_sbp, 
                             locations="ISO_Code", 
                             color="SBP", 
                             hover_name="Country", 
                             color_continuous_scale=px.colors.sequential.Plasma,
                             title="Countries with High SBP")

# Show the plot for countries with high SBP only
fig_high_sbp.show()