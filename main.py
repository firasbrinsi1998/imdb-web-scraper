#Make sure to include main.py and tools.py in the same directory

from tools import *

def main():
	
	year_list=[get_year(tg) for tg in moviestags]
	actors_list=[tg['title'] for tg in inner_moviestags]
	title_list=[tg.text for tg in inner_moviestags]
	rate_list=[tg['data-value'] for tg in rate_tags]
	movies_number=(len(rate_list))
	while True:
		index=random.randrange(0, movies_number)
		print(f'{title_list[index]}, starring {actors_list[index]}, released in {year_list[index]}, with a rating of  {float(rate_list[index]):.1f}' )
		answer=input('Do you want another suggestion(y/n)?\n')
		if answer!='y':
			break

	
if __name__ == '__main__':
    main()