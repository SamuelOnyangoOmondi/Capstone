import pandas as pd

# Define the dataset
data = {
    'Plastic_Waste_Input_kg': [10, 15, 8, 12, 10, 14, 9, 13, 11, 7, 16, 9, 10, 14, 15, 12, 8, 13, 11, 10],
    'Gas_Output_liters': [700, 1100, 540, 840, 650, 980, 610, 920, 770, 480, 1200, 620, 700, 1000, 1080, 840, 540, 900, 780, 680],
    'Efficiency_Percentage': [70, 73, 67, 70, 68, 71, 69, 72, 70, 66, 74, 68, 70, 71, 73, 69, 67, 71, 70, 70],
    'Temperature_C': [300, 305, 290, 298, 303, 307, 294, 302, 299, 285, 310, 297, 300, 308, 305, 299, 288, 307, 301, 300],
    'Pressure_kPa': [101, 105, 98, 100, 102, 103, 99, 104, 101, 97, 106, 100, 101, 104, 105, 102, 98, 103, 101, 101],
    'Methane_Composition': [60, 62, 58, 61, 59, 62, 60, 61, 60, 58, 63, 59, 60, 61, 62, 60, 59, 61, 60, 60],
    'Ethane_Composition': [25, 24, 26, 25, 25, 24, 25, 24, 25, 26, 24, 25, 25, 24, 24, 25, 25, 24, 25, 25],
    'Propane_Composition': [15, 14, 16, 14, 16, 14, 15, 15, 15, 16, 13, 16, 15, 15, 14, 15, 16, 15, 15, 15],
    'Carbon_Emissions_gkg': [100, 150, 80, 120, 105, 140, 90, 135, 110, 70, 160, 95, 100, 140, 150, 120, 80, 135, 110, 100],
    'Operating_Cost_USD': [15, 20, 12, 17, 15, 19, 13, 18, 16, 10, 21, 13, 15, 19, 20, 17, 12, 18, 16, 15],
    'Time_of_Production_minutes': [45, 50, 40, 46, 43, 47, 42, 48, 44, 39, 51, 42, 45, 47, 50, 46, 40, 47, 44, 45]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = 'plas_tech_complex_gas_production.csv'
df.to_csv(csv_file_path, index=False)

print(f"CSV file saved at: {"D:\Capstone\convert_to_csv.py"}")
