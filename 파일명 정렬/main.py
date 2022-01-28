# 프로그래머스 - 파일명 정렬
class UserFile:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.head = str()

        start = -1
        end = -1
        for i in range(len(self.file_name)):
            if self.file_name[i].isdigit():
                if start == -1:
                    start = i
                    end = i+1
                elif self.file_name[start:i].isdigit():
                    end = i+1

        self.number = int(file_name[start:end])
        self.head = file_name[:start].lower()
        self.tail = file_name[end:].lower()


def solution(file_names):
    files = [
        UserFile(file_name) for file_name in file_names
    ]
    files.sort(key=lambda x: (x.head, x.number))
    answer = [file.file_name for file in files]
    return answer

print(solution(	["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))