# Liam T
# Oct. 16 2013
# Unit 3 Option 1

length = input("length of prism: ")
width = input("width of prism: ")
height = input("height of prism: ")


def calculate_lr_area(length, height):
    """
    calculates the area of one side on the left/right axis
    :param length: length
    :param height: height
    :return: one left/right side area
    """
    one_lr_side_area = float(length) * float(height)
    return one_lr_side_area


def calculate_fb_area(width, height):
    """
    calculates the area of one side on the front/back axis
    :param width: width
    :param height: height
    :return: one front/back side area
    """
    one_fb_side_area = float(width) * float(height)
    return one_fb_side_area


def calculate_tb_area(length, width):
    """
    calculates the ares of one side on the top/bottom axis
    :param length: length
    :param width: width
    :return: one top/bottom side area
    """
    one_tb_side_area = float(length) * float(width)
    return one_tb_side_area


def calculate_total_surface_area(length, width, height):
    """
    calculates the total surface area of the prism
    :param length: length
    :param width: width
    :param height: height
    :return: total surface area
    """
    total_surface_area = (calculate_lr_area(length, width) * 2) + (calculate_fb_area(width, height) * 2) + (calculate_tb_area(length, width) * 2)
    return total_surface_area


lr = calculate_lr_area(length, height)
fb = calculate_fb_area(width, height)
tb = calculate_tb_area(length, width)

sa = calculate_total_surface_area(lr, fb, tb)

print("the total surface area of your prism is ", sa)
