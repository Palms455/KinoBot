from bs4 import BeautifulSoup
import requests




def get_html(url):
	r = requests.get(url)
	return r.text


def get_site_list(html):
	movies = {}
	soup = BeautifulSoup(html, 'lxml')
	items = soup.find('div', class_='td-page-content').find_all('table')
	date = items[0].find('strong').text
	for i in items[2:15:2]:
		for j in i.find_all('tr')[1:]:
			movie = j.find('a').text
			time = j.find('td').text
			if movie in movies:
				movies[movie].append(time)
			else: 
				movies[movie] = []
				movies[movie].append(time)
	return [date, movies]

def data(url):
	return get_site_list(get_html(url))


def main():
	url = 'https://cityopen.ru/afisha/kinotsentr-kinoport/'
	get_site_list(get_html(url))


if __name__ == '__main__':
	main()
