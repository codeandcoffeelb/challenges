#!/usr/bin/env bash

cat coffee.txt | convert -background white -size 1000x -fill black -font Courier -pointsize 12 caption:@- -trim -resize 50x -filter Box -resize 600x -auto-level coffee.png
open coffee.png