#!/usr/bin/env python
import json
import sys

def main():
  if len(sys.argv) != 2:
    print("Usage: python removeBuildingGeometry.py <INPUT FILE>")
    quit()

  filename = sys.argv[1]
  with open(filename) as json_data:
    d = json.load(json_data)

    # Iterate over all the features to find the one that needs altering
    newFeatures = list(filter(lambda x : x['properties']['type'] != "FLOOR", d['features']))
    sys.stderr.write(filename + ": removed " + str(len(d['features']) - len(newFeatures)) + " feature(s)\n")
    d['features'] = newFeatures
    print(json.dumps(d))

if __name__ == "__main__":
  main()

