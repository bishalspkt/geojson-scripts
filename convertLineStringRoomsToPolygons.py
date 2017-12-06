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
    changes = 0
    for feature in d['features']:
        geometryType = feature['geometry']['type']
        objectType = feature['properties']['type']

        if geometryType == "LineString" and objectType == "ROOM":
          changes += 1 
          feature['geometry']['type'] = "Polygon"
          feature['geometry']['coordinates'] = [feature['geometry']['coordinates']]

    sys.stderr.write(filename +": " + str(changes) + " features changed\n")
    print(json.dumps(d))

if __name__ == "__main__":
  main()

