"""
A module to provide some frequent functionalities for image data in one place

Author: Faruk Ahmad
Date: 23 May, 2020
Ref: #
"""

from PIL import Image
from numpy import asarray

"""
A dummpy method to read image in different color mode
"""
def read_image(img_path, mode = 'color'):
    if mode == "color":
        img_data = Image.open(img_path)
    elif mode == "gray":
        img_data = Image.open(img_path).convert('LA')
    elif mode == "black-white":
        img_data = Image.open(img_path).convert('L')

    return img_data


"""
A dummy method to convert image into numpy array
"""
def img_to_array(img_data):
    arr_data = asarray(img_data)

    return arr_data

"""
A dummy method to convet numpy array into image
"""
def array_to_image(arr_data):
    img_data = Image.fromarray(arr_data)

    return img_data

"""
A dummy method to save image
"""
def save_image(img_data, save_path):
    img_data.save(save_path)


if __name__ == "__main__":
    img_path = "./panda_org.jpg"

    img_data = read_image(img_path, mode='black-white')
    print(img_data.size)

    arr_data = img_to_array(img_data)
    print(arr_data.shape)

    img_data = array_to_image(arr_data)
    print(img_data.size)

    save_image(img_data, './panda_1.jpg')

