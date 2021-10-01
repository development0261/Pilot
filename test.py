
  

# import module
from geopy.geocoders import Nominatim
  
# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")
  
  
# Latitude & Longitude input
Latitude = "25.594095"
Longitude = "85.137566"
  

Latitude = "21.2074274"
Longitude = "72.7924497"

location = geolocator.reverse(Latitude+","+Longitude)
  
address = location.raw['address']
  
