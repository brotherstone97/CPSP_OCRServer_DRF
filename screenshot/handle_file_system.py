import os


def dir_size(path):
    # 해당 directory 내 파일의 total size
    total_size = 0
    with os.scandir(path=path) as dirEntry:
        # directory내 각 file에 대한 용량 추출(하위 directory는 생략)
        for entry in dirEntry:
            if entry.is_file():
                total_size += entry.stat().st_size  # st_size == file_size
    # total_size를  MB단위로 반환
    return total_size
