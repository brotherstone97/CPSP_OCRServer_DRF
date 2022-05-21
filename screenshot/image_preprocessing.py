# PIL
from PIL import Image
import os


def reduce_size(temp_path, new_path):
    image_list = os.listdir(temp_path)
    image_cnt = len(image_list)
    print(image_list)
    print(image_cnt)
    for name in image_list:
        file = temp_path + name
        img = Image.open(file)
        img.save(os.path.join(new_path, name),  optimize=True)
        # print(img.size)


reduce_size('../images/temp/', '../images/', 85)
###Quality 줄여선 용량의 변화가 없다