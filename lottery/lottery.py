import random

lottery_set = ('1','2','3','4','5','6','7','8','9','0','A','B','C','D','E')
winner_combination = ('8', 'C', '6', '2')


def get_lottery_combination():
	lottery_combination = []
	for i in range(4):
		lottery_combination.append(random.choice(lottery_set))
	return tuple(lottery_combination)


def lottery_check():
	"""Проверяет с какой попытки можно угадать выигрышную комбинацию"""
	win = False
	counter = 0

	while not win:
		counter += 1
		current_combination = get_lottery_combination()
		
		if current_combination == winner_combination:
			print(f'WIN! Counter - {counter}')
			win = True
		elif counter == 1_000_000:
			print(f'TIMEOUT! Counter - {counter}')
			break

if __name__ == '__main__':
	lottery_check()