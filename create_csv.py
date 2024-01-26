import csv
from datetime import datetime

# Get the current time
current_time = datetime.now().strftime("%H-%M-%S")

# Define the filename
filename = f"data/{current_time}.csv"

# Create a blank CSV file
with open(filename, 'w', newline='') as file:
  writer = csv.writer(file)
# You can write headers or data here if needed
