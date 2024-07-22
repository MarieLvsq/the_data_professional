import pandas as pd
import json
import plotly.express as px

# Load the Excel file
file_path = 'Transport_1314.xlsx'
excel_data = pd.ExcelFile(file_path)

# Function to clean and preprocess Table 6
def clean_table_6(sheet_name, skip_rows, n_rows, use_cols, col_names):
    df = excel_data.parse(sheet_name, skiprows=skip_rows, nrows=n_rows, usecols=use_cols)
    df.columns = col_names
    df.dropna(inplace=True)
    df[col_names[1:]] = df[col_names[1:]].apply(pd.to_numeric, errors='coerce')
    return df

# Preprocess Table 6
table_6 = clean_table_6('Table 6', skip_rows=3, n_rows=7, use_cols="B, C, E, G",
                        col_names=['Public_Services_Footprint', 'Mean', 'Lower_CI', 'Upper_CI'])

# Adjusting data to fit the new regions
region_mapping = {
    'North Wales': 'North Wales',
    'Mid and West': 'Mid and West Wales',
    'Swansea Bay': 'South Wales West',  # Mapping Swansea Bay to South Wales West
    'Cwm Taf': 'South Wales Central',   # Mapping Cwm Taf to South Wales Central
    'Cardiff and Vale': 'South Wales Central',  # Mapping Cardiff and Vale to South Wales Central
    'Gwent': 'South Wales East'  # Mapping Gwent to South Wales East
}

# Add a 'Region' column to match with GeoJSON region names
table_6['Region'] = table_6['Public_Services_Footprint'].map(region_mapping)

# Calculate the average for South Wales Central
south_wales_central = table_6[table_6['Region'] == 'South Wales Central']
south_wales_central_avg = south_wales_central[['Mean', 'Lower_CI', 'Upper_CI']].mean()

# Remove the individual entries and add the averaged entry
table_6 = table_6[table_6['Region'] != 'South Wales Central']
table_6 = table_6.append({
    'Public_Services_Footprint': 'South Wales Central',
    'Mean': south_wales_central_avg['Mean'],
    'Lower_CI': south_wales_central_avg['Lower_CI'],
    'Upper_CI': south_wales_central_avg['Upper_CI'],
    'Region': 'South Wales Central'
}, ignore_index=True)

# Save cleaned data
table_6.to_csv('cleaned_table_6.csv', index=False)

# Display the cleaned DataFrame
print("Cleaned Table 6:")
print(table_6)

# Load the converted GeoJSON file
with open('new_wales_regions.geojson') as f:
    geojson = json.load(f)

# Inspect the structure of the new GeoJSON file
print("GeoJSON structure:", list(geojson.keys()))

# Extract region names from the new structure
if 'features' in geojson:
    region_names_geojson = [feature['properties']['NAWER13NM'] for feature in geojson['features']]
    print("Region names in GeoJSON:", region_names_geojson)
else:
    print("GeoJSON does not contain 'features'. Please check the structure.")

# Plot the map
fig = px.choropleth(
    table_6,
    geojson=geojson,
    locations='Region',
    featureidkey="properties.NAWER13NM",  
    color='Mean',
    hover_name='Public_Services_Footprint',
    title='Overall Satisfaction with State of Transport System in Wales by Public Services Footprint'
)
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
