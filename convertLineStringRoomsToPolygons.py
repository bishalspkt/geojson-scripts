#!/usr/bin/env python
import json
import sys

def main():
  if len(sys.argv) != 2:
    print("Usage: python convertLineStringRoomsToPolygons.py <INPUT FILE>")
    quit()

  filename = sys.argv[1]
  with open(filename) as json_data:
    d = json.load(json_data)

    # Iterate over all the features to find the one that needs altering
    for feature in d['features']:
        geometryType = feature['geometry']['type']
        objectType = feature['properties']['type']

        if geometryType == "LineString" and objectType == "ROOM":
          sys.stderr.write(filename + ": Anomaly found!!\n")
          feature['geometry']['type'] = "Polygon"
          feature['properties']['editinfo'] = "Was LineString, is Polygon"
          feature['geometry']['coordinates'] = [feature['geometry']['coordinates']]

    print(json.dumps(d))

if __name__ == "__main__":
  main()

