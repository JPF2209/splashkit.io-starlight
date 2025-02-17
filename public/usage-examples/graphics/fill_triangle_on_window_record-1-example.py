from splashkit import *

blue_window = open_window("Blue Triangle", 200, 200)
red_window = open_window("Red Triangle", 200, 200)
move_window_to(red_window, window_x(blue_window) + window_width(blue_window), window_y(blue_window))

# Define the triangles to draw
blue_triangle = triangle_from(point_at(50, 100), point_at(100, 50), point_at(150, 100))
red_triangle =  triangle_from(point_at(50, 50), point_at(100, 100), point_at(150, 50))

# Fill a blue triangle on the first window
clear_window(blue_window, color_white())
fill_triangle_on_window_record(blue_window, color_blue(), blue_triangle)
refresh_window(blue_window)

# Fill a red triangle on the second window
clear_window(red_window, color_white())
fill_triangle_on_window_record(red_window, color_red(), red_triangle)
refresh_window(red_window)

delay(10000)

close_window(blue_window)
close_window(red_window)