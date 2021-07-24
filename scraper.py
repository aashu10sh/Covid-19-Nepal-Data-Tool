from bs4 import BeautifulSoup
import requests
import time
import datetime


class CovidUpdateGetter:
    def __init__(self, url):
        self.url = url
        self.source = requests.get(self.url).text
        print('Nepal Covid 19 Update Tool')
        print('Fetching Data From The Server, Please wait a moment..')
        time.sleep(4)

    def get_value_from_html(self):
        self.soup = BeautifulSoup(self.source, 'lxml')
        total_cases_div = self.soup.find_all(
            'div', class_='maincounter-number')
        total_cases = total_cases_div[0].span.text
        total_deaths = total_cases_div[1].span.text
        total_recovered = total_cases_div[2].span.text

        return total_cases, total_deaths, total_recovered

    def get_the_last_day(self):
        latest_news_div_name = "newsdate" + \
            str(datetime.date.today() - datetime.timedelta(days=1))
        latest_news = self.soup.find_all('div', class_=str('row'))
        news_new_main_div = latest_news[10]
        main_div = news_new_main_div.find('div', id=latest_news_div_name)
        last24_hours_cases = main_div.ul.strong.text
        return last24_hours_cases

    def print_values_and_exit(self, tc, td, tr, nc):
        print(f"Total Cases : {tc}")
        print(f"Total Deaths : {td}")
        print(f"Total Recovered : {tr}")
        print(f"{nc} in the last 24 hours")

    def main(self):
        self.total, self.death, self.recovered = self.get_value_from_html()
        self.lasthours = self.get_the_last_day()
        self.print_values_and_exit(
            self.total, self.death, self.recovered, self.lasthours)


if __name__ == "__main__":
    worldmeter = CovidUpdateGetter(
        'https://www.worldometers.info/coronavirus/country/nepal')
    worldmeter.main()
