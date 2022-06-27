# PIL
from PIL import Image
import os

def reduce_size(temp_path, new_path, filename):
    # typecast
    filename = str(filename)
    file = temp_path + filename
    img = Image.open(file)
    # optimizing 후 이미지 재저장
    img.save(os.path.join(new_path, filename), optimize=True)
    # 기존 이미지 삭제
    os.remove(file)
