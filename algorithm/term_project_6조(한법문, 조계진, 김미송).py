# 6조 텀프로젝트
# 한법문, 조계진, 김미송

class Omok:
	
	def __init__(self):
		self.turn = 0
		self.init_board() 
		self.determine_order()
		self.auto = self.init_player()
		self.player = self.init_player()


	def init_board(self):		#오목 판 생성
		self.board = dict()
		for row in range(0, 20):
			if (row == 0):
				self.board[str(row)] = '-'
			else:
				temp = dict()
				for col in range(ord('A'), ord('T')):
					temp[chr(col)] = '.'
				self.board[str(row)] = temp
	
	def init_player(self):
		player = dict()
		for r in range(1, 20):
			player[str(r)] = [False for _ in range(0, 20)]
		return player
	
	def draw_board(self):
		for r in range(len(omok.board) - 1, 0, -1):
			for c in range(ord('A'), ord('T')):
				print(omok.board[str(r)][chr(c)], end="  ")
			print("")

	def determine_order(self):
		while True:
			self.order = input("선공 후공을 선택해주세요 || 선공 : 0, 후공 : 1 입력\n")
			if (self.order == '0' or self.order == '1'):
				self.order = int(self.order)
				break
			print("입력 양삭을 다시 확인해주세요.\n선공 : 0 || 후공 : 1\n")
		if (self.order == 0):
			self.auto_stone = '●'
			self.player_stone = '○'
			print("선공!!")
		else:
			self.auto_stone = '○'
			self.player_stone = '●'
			print("후공!!")
	
	
	# 체크 관련 함수
	def check_input(self, coord):
		if (len(coord) != 2) or not (coord[0].isdecimal()):
			return (False)
		elif (0 < int(coord[0]) < 20) and (len(coord[1]) == 1 and 'A' <= coord[1] < 'T'):
			return (True)
		else:
			return (False)
	
	def check_filled(self, coord):
		if not (self.board[coord[0]][coord[1]] == '.'):
			return (True)
		return (False)
	
	def check_horizontal(self, who, num):        #가로 체크
		result = False
		for r in range(1, 20):
			cnt = 0
			for c in range(0, 19):
				if (who[str(r)][c]):
					cnt += 1
				else:
					if (cnt == num):
						sides = [[str(r), chr(ord('A') + c - num - 1)], [str(r), chr(ord('A') + c)]]    # 양 옆 돌 위치
						if not (self.check_input(sides[0])):
							del sides[0]
						if (len(sides) == 2):
							s1 = sides[0]
							s2 = sides[1]
							if (self.board[s1[0]][s1[1]] == '.' and self.board[s2[0]][s2[1]] == '.'):   # 양 쪽 둘다 비었으면 둘 중 하나 바로 리턴
								return (sides)
						for s in sides:
							if (self.board[s[0]][s[1]] == '.'):     #사이드에 있는 것 중 빈 곳 있으면 저장
								result = [s]
					cnt = 0
			if (cnt == num):
				side = [str(r), chr(ord('A') + 18 - num)]
				if (self.board[side[0]][side[1]] == '.'):
					result = [side]
		return (result)
	
	def check_vertical(self, who, num):            #세로 체크
		result = False
		for c in range(0, 19):
			cnt = 0
			for r in range(1, 20):
				if (who[str(r)][c]):
					cnt += 1
				else:
					if (cnt == num):
						sides = [[str(r), chr(ord('A') + c)], [str(r - num - 1), chr(ord('A') + c)]]
						if not (self.check_input(sides[0])):
							del sides[0]
						if (len(sides) == 2):
							s1 = sides[0]
							s2 = sides[1]
							if (self.board[s1[0]][s1[1]] == '.' and self.board[s2[0]][s2[1]] == '.'):   # 양 쪽 둘다 비었으면 둘 중 하나 바로 리턴
								return (sides)
						for s in sides:
							if (self.board[s[0]][s[1]]) == '.':
								result = [s]
					cnt = 0
			if (cnt == num):
				side = [str(19 - num), chr(ord('A') + c)]
				if (self.board[side[0]][side[1]] == '.'):
					result = [side]
		return (result)
	
	def check_diagonal_up(self, who, num):        # / 방향 체크
		result = False
		for r in range(1, 21 - num):
			cnt = 0
			for c in range(0, 20 - r):
				if (who[str(r + c)][c]):
					cnt += 1
				else:
					if (cnt == num):
						sides = [[str(r + c - num - 1), chr(ord('A') + c - num - 1)], [str(r + c), chr(ord('A') + c)]]
						if not (self.check_input(sides[0])):
							del sides[0]
						if (len(sides) == 2):
							s1 = sides[0]
							s2 = sides[1]
							if (self.board[s1[0]][s1[1]] == '.' and self.board[s2[0]][s2[1]] == '.'):   # 양 쪽 둘다 비었으면 둘 중 하나 바로 리턴
								return (sides)
						for s in sides:
							if (self.board[s[0]][s[1]]) == '.':
								result = [s]
					cnt = 0
			if (cnt == num):
				side = [str(19 - num), chr(ord('A') + 19 - r - num)]
				if (self.board[side[0]][side[1]] == '.'):
					result = [side]
		for c in range(1, 20 - num):
			cnt = 0
			for r in range(1, 20 - c):
				if (who[str(r)][c + r - 1]):
					cnt += 1
				else:
					if (cnt == num):
						sides = [[str(r - num - 1), chr(ord('A') + c + r - num - 2)], [str(r), chr(ord('A') + c + r - 1)]]
						if not (self.check_input(sides[0])):
							del sides[0]
						if (len(sides) == 2):
							s1 = sides[0]
							s2 = sides[1]
							if (self.board[s1[0]][s1[1]] == '.' and self.board[s2[0]][s2[1]] == '.'):   # 양 쪽 둘다 비었으면 둘 중 하나 바로 리턴
								return (sides)
						for s in sides:
							if (self.board[s[0]][s[1]]) == '.':
								result = [s]
					cnt = 0
			if (cnt == num):
				side = [str(19 - c - num), chr(ord('A') + 18 - num)]
				if (self.board[side[0]][side[1]] == '.'):
					result = [side]
		return (result)
	
	def check_diagonal_down(self, who, num):        # \ 방향 체크
		result = False
		for r in range(num, 20):
			cnt = 0
			for c in range(0, r):
				if (who[str(r - c)][c]):
					cnt += 1
				else:
					if (cnt == num):
						sides = [[str(r - c + num + 1), chr(ord('A') + c - num - 1)], [str(r - c), chr(ord('A') + c)]]
						if not (self.check_input(sides[0])):
							del sides[0]
						if (len(sides) == 2):
							s1 = sides[0]
							s2 = sides[1]
							if (self.board[s1[0]][s1[1]] == '.' and self.board[s2[0]][s2[1]] == '.'):   # 양 쪽 둘다 비었으면 둘 중 하나 바로 리턴
								return (sides)
						for s in sides:
							if (self.board[s[0]][s[1]]) == '.':
								result = [s]
					cnt = 0
			if (cnt == num):
				side = [num + 1, chr(ord('A') + r - num - 1)]
				if (self.board[side[0]][side[1]] == '.'):
					result = [side]
		for c in range(19 - num, 0, -1):
			cnt = 0
			for r in range(0, 19 - c):
				if (who[str(19 - r)][c + r]):
					cnt += 1
				else:
					if (cnt == num):
						sides = [[str(19 - r + num + 1), chr(ord('A') + c + r - num - 1)], [str(19 - r), chr(ord('A') + c + r)]]
						if not (self.check_input(sides[0])):
							del sides[0]
						if (len(sides) == 2):
							s1 = sides[0]
							s2 = sides[1]
							if (self.board[s1[0]][s1[1]] == '.' and self.board[s2[0]][s2[1]] == '.'):   # 양 쪽 둘다 비었으면 둘 중 하나 바로 리턴
								return (sides)
						for s in sides:
							if (self.board[s[0]][s[1]]) == '.':
								result = [s]
					cnt = 0
			if (cnt == num):
				side = [str(c + 1 + num), chr(ord('A') + 18 - num)]
				if (self.board[side[0]][side[1]] == '.'):
					result = [side]
		return (result)
			
	def check_win(self, who):
		if (self.check_horizontal(who, 5)):
			print(self.check_horizontal(who, 5))
			return (True)
		elif (self.check_vertical(who, 5)):
			print(self.check_vertical(who, 5))
			return (True)
		elif (self.check_diagonal_up(who, 5)):
			print(self.check_diagonal_up(who, 5))
			return (True)
		elif (self.check_diagonal_down(who, 5)):
			print(self.check_diagonal_down(who, 5))
			return (True)
		return (False)
				
 
	# 돌 놓는 함수 모음
	def put_first_stone(self):
		self.turn += 1
		if (self.board['10']['J']) == '.':
			self.auto['10'][ord('J') - ord('A')] = True     # 선공시 첫 시작 가운데 돌
			self.board['10']['J'] = self.auto_stone
			print("#"*30)
			print("auto_put: ['10', 'J']")
			print("#"*30)
		else:
			self.auto['10'][ord('K') - ord('A')] = True     # 선공시 첫 시작 가운데 돌
			self.board['10']['K'] = self.auto_stone
			print("#"*30)
			print("auto_put: ['10', 'K']")
			print("#"*30)
 
	def put_stone(self, who, coord, stone):
		who[coord[0]][ord(coord[1]) - ord('A')] = True
		self.board[coord[0]][coord[1]] = stone
 
	def put_player_stone(self, coord):
		self.turn += 1

		self.put_stone(self.player, coord, self.player_stone)
		
	def put_auto_stone(self):
		self.turn += 1
		
		for i in range(4, 0, -1):
			#공격
			hor = self.check_horizontal(self.auto, i)
			if not (hor):
				hor = []
			ver = self.check_vertical(self.auto, i)
			if not (ver):
				ver = []
			dia_up = self.check_diagonal_up(self.auto, i)
			if not (dia_up):
				dia_up = []
			dia_down = self.check_diagonal_down(self.auto, i)
			if not (dia_down):
				dia_down = []
			coord_list = [hor, ver, dia_up, dia_down]
			len_list = [len(hor), len(ver), len(dia_up), len(dia_down)]
			max_len_i = len_list.index(max(len_list))
			coord = coord_list[max_len_i]
			if (len(coord) != 0):
				coord = coord[0]
				print("#"*30)
				print("auto_put: ", coord)
				print("#"*30)
				return (self.put_stone(self.auto, coord, self.auto_stone))
			
			##수비
			hor = self.check_horizontal(self.player, i)
			if not (hor):
				hor = []
			ver = self.check_vertical(self.player, i)
			if not (ver):
				ver = []
			dia_up = self.check_diagonal_up(self.player, i)
			if not (dia_up):
				dia_up = []
			dia_down = self.check_diagonal_down(self.player, i)
			if not (dia_down):
				dia_down = []
			coord_list = [hor, ver, dia_up, dia_down]
			len_list = [len(hor), len(ver), len(dia_up), len(dia_down)]
			max_len_i = len_list.index(max(len_list))
			coord = coord_list[max_len_i]
			if (len(coord) != 0):
				coord = coord[0]
				print("#"*30)
				print("auto_put: ", coord)
				print("#"*30)
				return (self.put_stone(self.auto, coord, self.auto_stone))
			
			
omok = Omok()

if (omok.order == 0):
	omok.put_first_stone()

while (omok.turn < 362):
	###상대방 돌 놓기###
	player_coord = input("돌을 놓을 좌표를 입력해주세요. | ex) 1,A \n").upper().split(',')
	if not (omok.check_input(player_coord)):
		print("입력 좌표를 다시 확인해주세요!")
		print("row : 1 ~ 19 || col : A ~ S")
		continue
	if (omok.check_filled(player_coord)):
		print("이미 채워진 곳입니다!")
		# continue
		break
	omok.put_player_stone(player_coord)
	#################
	
	if (omok.turn == 1):
		omok.put_first_stone()
	else:
		omok.put_auto_stone()
	
	print("진행횟수 : ", omok.turn)
	omok.draw_board()
	if (omok.check_win(omok.player)):
		print("player Win!!")
		break
	elif (omok.check_win(omok.auto)):
		print("auto Win!!")
		break
print("finish")