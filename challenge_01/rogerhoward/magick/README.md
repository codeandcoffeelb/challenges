# c2i using Imagemagick

```
cat coffee.txt | convert -background white -size 1000x -fill black -font Courier -pointsize 12 caption:@- -trim -resize 50x -filter Box -resize 600x -auto-level coffee.png
```

Play-by-play

`-background white -size 1000x` creates a 1000 pixel wide document with white background, intentionally extra-wide because we'll trim it later.

`fill black -font Courier -pointsize 12 caption:@-` draws the text received on stdin (from cat)

`-trim -resize 50x` crops the document tightly to the text and then resizes it to 50 pixels wide to effectively reduce the characters to indvidual pixels. The 50 pixel value was picked empirically by testing a range of values from 30-100px.

`-filter Box -resize 600x` now we scale back up to any arbitrary size, using the Box filter to maintain the pixellation.

`-auto-level` This scales the levels of the image so the darkest tone becomes black and the lightest becomes white.