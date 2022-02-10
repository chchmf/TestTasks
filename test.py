#task1


def find_top_20(candidates):
	candidates_dict = {}
	for i in candidates:
		name = i["name"]
		score = sum(i["scores"].values()) + i["extra_scores"]
		candidates_dict.update({name : score})

	candidates_sort = sorted(candidates_dict.items(),key= lambda  x: (-x[1],x[0]))

	names_top = []

	for i in candidates_sort:
		only_name = list(i)[0]
		names_top.append(only_name)

	return names_top[:20]


#task2


def get_inductees(names, birthday_years, genders):
	if len(names) == len(birthday_years) & len(names) == len(genders):
		valid_names = []
		invalid_names = []	

		for i in range(len(names)):
			if birthday_years[i] == None or genders == None:
				invalid_names.append(names[i])
			else:
				age = 2021 - birthday_years[i]
				if  18 <= age <= 30:
					valid_names.append(names[i])

		return valid_names, invalid_names
	
	else:
		print("Списки разной длины")


#task3


""" Сначала сделал так. Но после того как получил ОС о том что надо было использовать set, переделал
def find_athlets(know_english, sportsmen, more_than_20_years):
	all_matches = []
	for i in know_english:
		if i in sportsmen and i in more_than_20_years:
			all_matches.append(i)
		else:
			pass
	return all_matches
"""

def find_athlets(know_english, sportsmen, more_than_20_years):
	return list(set(know_english) & set(sportsmen) & set(more_than_20_years))
	

#task3


import os

def make_report_about_top3(students_avg_scores):
	students_avg_scores_sort = sorted(students_avg_scores.items(),
									key= lambda  x: (-x[1],x[0]))
	with open("top3.csv", "w") as file:
		file.write(f"Имя,Средний балл\n")
		for i in students_avg_scores_sort[:3]:
			file.write(f"{list(i)[0]},{list(i)[1]}\n")
	return os.path.abspath('top3.csv')
