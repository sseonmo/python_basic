""""
# os.access(path, mode)
#  - 입력받은 path 에 대해서 mode에 대당하는 작업이 가능한지 여부를 반환한다.
# > F_OK  : 해당 path 존재여부
# R_OK : 읽기
# X_OK : 실행
# W_OK : 쓰기

- os.listdir(path)
- os.mkdir(path[, mode])
- os.makedirs(path[, mode])
- os.remove(path), os.unlink(path)
	파일을 삭제
- os.rmdir(path)
	디렉토리삭제 - 단 디렉토리가 비워잇어야 삭제가능
- os.removedirs(path)
	디렉토리를 순차적으로 삭제
- os.rename(src, dst)
	파일, 디렉토리 모두 적용됨
- os.utime(path, times)
	times None 경우 현재시간으로 수정
- ow.walk
	* topdown이 False 입력되면 desc으로 검색
- os.pipe() ??



"""