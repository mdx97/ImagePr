------------------
CARTOON.PY
------------------

Objective
--------
Main objective is to group pixels that are of similar color into regions. Then, create a mean color for the region. The region will then be filled with that color.

Design
--------
* Building Regions *
1. Use the matrix representation of the image (I). Each pixel will be represented by a tuple containing RGB values. [(R, G, B)]
2. Use a second matrix to represent regions (called R). This matrix will be initialized with 0s. Regions will begin with the number 1.
3. We will define a list (C) which will store the colors for each region.
4. To detect our regions. We will pick the index of the first 0 in R. (This is the first pixel that is not a member of a region yet.)
5. Conduct a BFS on adjacent pixels. Use the the color of the pixel picked in step 3 to determine which pixels will be added to the region.
6. Set all the values for the selected pixels to the number of the region in R.
7. Average the color of all the pixels selected, add that value to C for the current region.

* Building the New Image *
1. We will use the I matrix, since there is no need to create a new matrix. Loop through each pixel and get the region it is apart of from R. Then set the color of the pixel to the value cooresponding to the region selected from R from C.
2. Save the new image!

Notes
-------
- Need to find a better way to detect the regions or modify the existing method. The current method results in some odd region patterns.