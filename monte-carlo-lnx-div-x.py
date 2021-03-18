import math
import random

# calculate integral of ln(x)/x
#idea is to draw a box over integrated function and count all the random points that we generate in that box - which of them are in the integral place, and which outside,
#then calculate (in_area/all_points_randomly_generated_in_box) * box_area 

#integral is about 2.650949055239199

def integrated_function(x):
    return math.log(x) / x

count = 0.0
in_area = 0.0

while count < 1000000:
    x = random.uniform(1, 10)
    y = random.uniform(0, 1/math.e)

    if y < integrated_function(x):
        in_area += 1

    count += 1

area_box_max_height = math.e #max hight of function in the domain scope
area_box_width = 10 - 1 #it is because 0 point for function is in x = 1, and our domain is <1,10>
area_box = area_box_width / area_box_max_height

print ((in_area / count) * area_box)
