# PIL
from PIL import Image
import os
from django.utils import timezone


def reduce_size(temp_path, new_path, filename):
    # typecast
    old_filename = str(filename)

    # 기존 이미지 파일명
    temp_file = temp_path + old_filename
    img = Image.open(temp_file)
    # 새로 저장할 파일명
    new_filename = get_new_filename(old_filename)
    # 새로 저장할 파일의 최종 경로(새 디렉토리 + 새 파일명)
    final_file_path = os.path.join(new_path, new_filename)
    extra_int = 1
    # 이미 파일명이 존재할 경우 존재하지 않은 이름이 나올 때까지 무한루프(요청이 초단위까지 같을 경우를 고려)
    while True:
        # 파일명이 중복일 때
        if os.path.isfile(final_file_path):
            new_filename = get_new_filename(old_filename, f'({extra_int})')
            final_file_path = os.path.join(new_path, new_filename)
            # 붙여줄 번호 + 1
            extra_int += 1
        else:
            # optimizing 후 이미지 재저장
            img.save(fp=final_file_path, optimize=True)
            # 기존 이미지 삭제
            os.remove(temp_file)
            break


# 저장된 시간이 적힌 새 이름으로 바꾸기 위한 함수
def get_new_filename(old_filename, extra_str=''):
    # 현재 시각
    datetime_now = timezone.now().strftime("%Y-%m-%d-%H-%M-%S")
    # .이 나오는 위치
    index_of_dot = old_filename.index('.')
    # 확장자 추출
    file_extension = old_filename[index_of_dot:]
    new_filename = datetime_now + extra_str + file_extension

    # 파일명 예) 2022-06-28-00-00-00.jpg
    return new_filename
