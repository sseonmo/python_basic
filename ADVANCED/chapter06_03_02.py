# Chapter06_03_01
# 파이썬 심화
# Future 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 동시성 활용 권장
# 적합한 작업일 경우 순차 진행보다 압도적으로 성능 향상

# 실슴 대상 3가지 경우

# 순차실행
# concurrent.futures 방법1
# concurrent.futures 방법2

# Google Python GIL(Global Interpreter Lock)
# Gil 은 한번에 하나의 스레드만 수행 할 수 있게 인터프리터 자체에서 락을 거는 것.

import os
import time
import sys
import csv
from concurrent import futures

# Concurrent.future 방법1(ThreadPoolExceutor, ProcessPoolExecutor(CPU 이용))
# map()
# 서로다른 스레드 또는 프로세스에서 실행 가능
# 내부 과정을 알 필요없으며, 고수준으로 인터페이스 제공
# 국가정보
NATION_LS = 'Singapore Germany Israel Norway Italy Canada France Spain Mexico'.split()
# 초기 CSV 위치
TARGET_CSV = os.path.join(os.path.dirname(__file__), 'resources', 'nations.csv')
# 저장폴더위치
DEST_DIR = os.path.join(os.path.dirname(__file__), 'csvs')
# CSV 헤더 기초 정보
HEADER = 'Region,Country,Item Type,Sales Channel,Order Priority,Order Date,Order ID,Ship Date,Units Sold,Unit Price,Unit Cost,Total Revenue,Total Cost,Total Profit'.split(',')

# 파일내용
CSV_CONTENT = []

with open(TARGET_CSV, 'r') as f:
	reader = csv.DictReader(f)
	for r in reader:
		CSV_CONTENT.append(r)

# ThreadPoolExecutor 사용함 - 파일내용을 읽어 변수 저장 후 시간을 재어봣을때 엄청난 차이가 난다.
# ['Canada', 'France', 'Germany', 'Israel', 'Italy', 'Mexico', 'Norway', 'Singapore', 'Spain'] csv separated in 16.46s
# ['Canada', 'France', 'Germany', 'Israel', 'Italy', 'Mexico', 'Norway', 'Singapore', 'Spain'] csv separated in 0.61s

# 국가별 CSV 파일저장
def save_csv(data, filename):
	# 최종 경로 생성
	path = os.path.join(DEST_DIR, filename)

	with open(path, 'w', newline='') as fp:
		writer = csv.DictWriter(fp, fieldnames=HEADER)
		# Header Writer
		writer.writeheader()
		# Dict to CSV Write
		for row in data:
			writer.writerow(row)

# 국가별 분리
def get_sales_data(nt):

	with open(TARGET_CSV, 'r') as f:
		reader = csv.DictReader(f)
		# Dict을 리스트로 적재
		data = []
		# Header 확인
		# print(reader.fieldnames)
		for r in reader:
			# orderDict
			# print(r)
			# 조건에 맞는 국가만 삽입
			if r['Country'] == nt:
				# print(r['Country'])
				data.append(r)
	return data

def get_sales_data1(nt):

	data = []
	for r in CSV_CONTENT:
		if r['Country'] == nt:
			data.append(r)

	return data

# 중간상황출력
def show(text):
	print(text, end=' | ')
	# 중간 출력(버퍼 비우기)
	sys.stdout.flush()

# 국가 별 문리 함수 실행
def separate_many(nt):

	# 분리데이터
	data = get_sales_data1(nt)
	# 상황 출력
	show(nt)
	# 파일 저장
	save_csv(data, nt.lower() + '.csv')
	return nt

# 시간 측정 및 메인함수
def main(separate_many):
	# worker 개수
	worker = min(20, len(NATION_LS))
	# 시작시간
	start_time = time.time()

	# 결과견수
	# ThreadPoolExecuotr : GIL 종속
	# ProcessPoolExecutor : GIL 우회, 변경 후 -> os.cpu_count()을 이용해 cpu갯수를 자동 셋팅한다.
	with futures.ThreadPoolExecutor(worker) as executor:
	# with futures.ProcessPoolExecutor() as executor:
		# map -> 작성 순서 유지, 즉시 실행
		result_cnt = executor.map(separate_many, sorted(NATION_LS))

	# 종료시간
	end_tm = time.time() - start_time

	msg = '\n{} csv separated in {:.2f}s'
	print(msg.format(list(result_cnt), end_tm))

# 실행
if __name__ == '__main__':
	main(separate_many)


