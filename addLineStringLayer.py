#!/usr/bin/env python
import json
import sys

def main():
    if len(sys.argv) < 2:
        print ("Usage: python script.py <INPUT FILE>")
    else:
        filename = sys.argv[1]
        with open(filename) as json_data:
            d = json.load(json_data)

            # Take the feature of first polygon
            feature = d['features'][0]
            lineString = {}
            lineString['type'] = 'Feature'

            geometry = {}
            geometry['type'] = "LineString"
            geometry['coordinates'] =feature['geometry']['coordinates'][0]
            
            properties = {}
            '''
            properties['type'] = 'AUTO-GEN-BORDER'
            properties['stroke'] = 'red'
            properties['stroke-width'] = 2
            properties['stroke-opacity'] =1 
            '''

            lineString['geometry'] = geometry
            lineString['properties'] = properties
            d['features'].append(lineString)
            print(json.dumps(d))

if __name__ == "__main__":
    main()
