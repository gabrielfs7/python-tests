from geopy.geocoders import Nominatim
import pandas

"""

Import "Nominatim" for geocoding.

"""
nominatim=Nominatim(scheme="http")

"""

Here we can get a "Location" object containing latitude and longitude.

"""
nominatim.geocode("3995, 23rd St, San Francisco, CA 94114")

"""

- Load file to a DataFrame.
- Create a new column "Coordinates" to store complete address.
- Apply "nominatim.geocode" for column "Coordinates" on each row.
- Call a "lambda" function to get "lagitude" or "longitude" if not "None"

"""
df = pandas.read_csv("../data_analysis/supermarkets.csv")
df['Coordinates'] = df['Address'] + ", " + df['City'] + ", " + df['State'] + ", " + df["Country"]
df['Coordinates'] = df['Coordinates'].apply(nominatim.geocode)
df['Latitude'] = df['Coordinates'].apply(lambda column_value: column_value.latitude if column_value != None else None)
df['Longitude'] = df['Coordinates'].apply(lambda column_value: column_value.longitude if column_value != None else None)
df