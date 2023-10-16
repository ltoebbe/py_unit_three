# Liam Toebbe
# Oct. 16 2013
# Unit 3 Option 1

length = input("length of prism: ")
width = input("width of prism: ")
height = input("height of prism: ")


def calculate_lr_area(length, height):
    one_lr_side_area = float(length) * float(height)
    return one_lr_side_area


def calculate_fb_area(width, height):
    one_fb_side_area = float(width) * float(height)
    return one_fb_side_area


def calculate_tb_area(length, width):
    one_tb_side_area = float(length) * float(width)
    return one_tb_side_area


def calculate_total_surface_area(length, width, height):
    total_surface_area = (calculate_lr_area(length, width) * 2) + (calculate_fb_area(width, height) * 2) + (calculate_tb_area(length, width) * 2)
    return total_surface_area


lr = calculate_lr_area(length, height)
fb = calculate_fb_area(width, height)
tb = calculate_tb_area(length, width)

sa = calculate_total_surface_area(lr, fb, tb)

print("the total surface area of your prism is ", sa)
