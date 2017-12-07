#!/usr/bin/env python
import json
import sys

'''
    Changes ROOM objects drawn by LineString to Polygons. It also does a sanity
    check to verify if the polygon in valid geojson.
    
    Checks include:
    Count number of points in a ring. Check if it is greater than or equals to 4
    Check if the ring is closed
'''
def main():
  if len(sys.argv) != 2:
    print("Usage: python convertLineStringRoomsToPolygons.py <INPUT FILE>")
    quit()

  filename = sys.argv[1]
  with open(filename) as json_data:
    d = json.load(json_data)

    # Iterate over all the features to find the one that needs altering
    changes = 0
    # Do a list comprehension to remove invalids
    newFeatures = [feature for feature in d['features'] if filterCondition(feature)]
    removals = len(d['features']) - len(newFeatures)
    d['features'] = newFeatures

    for feature in d['features']:
        geometryType = feature['geometry']['type']
        objectType = feature['properties']['type']

        if geometryType == "LineString" and objectType == "ROOM":
          changes += 1 
          feature['geometry']['type'] = "Polygon"
          feature['geometry']['coordinates'] = checkCoordinates(feature['geometry']['coordinates'])

    sys.stderr.write(filename +": " + str(changes) + " features changed. "+ str(removals) + " features removed" +"\n")
    
    print(json.dumps(d))

def filterCondition(feature):
  if feature['properties']['type'] == 'ROOM' and feature['geometry']['type'] == 'LineString' and len(feature['geometry']['coordinates']) < 4:
    return False
  return True

def checkCoordinates(c):
  if c[0] != c[-1]:
    c.append(c[0])
  return [c]

if __name__ == "__main__":
  main()

