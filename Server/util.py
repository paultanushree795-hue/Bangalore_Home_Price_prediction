import json
import pickle
import numpy as np

#These are 3 global variables I've
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
   try:

        loc_index = __data_columns.index(location.lower()) #In a python list to find an index you can call .index() method
   except:

       loc_index = -1

   x = np.zeros(len(__data_columns))
   x[0] = sqft
   x[1] = bath
   x[2] = bhk
   if loc_index >= 0:
        x[loc_index] = 1
   return round(__model.predict([x])[0],2)

# 1st Routine
def get_location_names(): #It just returns the location names
    return __locations

def load_saved_artifacts(): #This method will load the saved artifacts which is my cols of JSON
          print("Loading saved artifacts...start")                   #and Bengalore home prices
          global __data_columns
          global __locations

          with open("./artifacts/columns.json", "r") as f:
              __data_columns = json.load(f) ["data_columns"]
              __locations = __data_columns[3:]
          global __model
          with open("./artifacts/complex_model", "rb") as f:
                __model = pickle.load(f)
          print("Loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("1stPhase JP Nagar",1000,3,3))
    print(get_estimated_price("1stPhase JP Nagar",1000,2,2))
    print(get_estimated_price("Kalhalli",1000,2,2)) #Other location
    print(get_estimated_price("Ejipura",1000,2,2)) #Other location

