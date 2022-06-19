from tools import *

def main():
	response = requests.get(url)
	html=response.text

	soup=BeautifulSoup(html,'html.parser')
	moviestags=soup.select('td.titleColumn')
	inner_moviestags=soup.select('td.titleColumn a')
	inner_moviestag=inner_moviestags[0]

	def get_year(movie_tag):
		moviesplit=movie_tag.text.split()
		year=moviesplit[-1]
		return year

	year_list=[get_year(tg) for tg in moviestags]
	actors_list=[tg['title'] for tg in inner_moviestags]
	title_list=[tg.text for tg in inner_moviestags]
	print(title_list)
if __name__ == '__main__':
    main()