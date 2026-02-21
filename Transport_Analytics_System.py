import pandas as pd
#vehicle details
vehicle_df = pd.read_csv("Vehicle_details.csv")
print("Vehicle Details:")
print(vehicle_df.head())
#Driver logs
driver_logs_df = pd.read_csv("Driver_logs.csv")
print("Driver Logs:")
print(driver_logs_df.head())
#GPS Route Logs
GPS_routes_df = pd.read_csv("GPS_routes_logs.csv")
print("GPS Routes:")
print(GPS_routes_df.head())
#Fuel Logs
fuel_logs_df = pd.read_csv("Fuel_logs.csv")
print("Fuel Logs:")
print(fuel_logs_df.head())
#Delivery Timelines
delivery_logs_df = pd.read_csv("Delivery_timelines.csv")
print("Delivery Timelines:")
print(delivery_logs_df.head())
#Maintenance History
maintenance_history_df = pd.read_csv("Maintenance_history.csv")
print("Maintenance History:")
print(maintenance_history_df.head())

