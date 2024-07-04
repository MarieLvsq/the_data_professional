import pandas as pd
import plotly.express as px

# Load the CSV file into a DataFrame
file_path = '2_bloodpressure_plotly.csv'
blood_pressure_data = pd.read_csv(file_path)

# Create the animated scatter plot
fig = px.scatter(blood_pressure_data, 
                 x="Mean systolic blood pressure (mmHg)", 
                 y="Mean diastolic blood pressure (mmHg)", 
                 animation_frame="Year",  
                 color="Sex",  
                 hover_name="Country/Region/World",  
                 range_x=[blood_pressure_data["Mean systolic blood pressure (mmHg)"].min(), blood_pressure_data["Mean systolic blood pressure (mmHg)"].max()],
                 range_y=[blood_pressure_data["Mean diastolic blood pressure (mmHg)"].min(), blood_pressure_data["Mean diastolic blood pressure (mmHg)"].max()],
                 title="Blood Pressure Over Time",
                 labels={"Mean systolic blood pressure (mmHg)": "Systolic Blood Pressure", 
                         "Mean diastolic blood pressure (mmHg)": "Diastolic Blood Pressure"})

fig.show()
