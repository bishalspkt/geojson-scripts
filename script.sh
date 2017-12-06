#!/bin/bash
for filename in input/*.json; do
  python convertLineStringRoomsToPolygons.py "$filename" > "output/$(basename "$filename" .json)_LTP.json"
done
