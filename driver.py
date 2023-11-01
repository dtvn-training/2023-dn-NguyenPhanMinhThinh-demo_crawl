import requests
from bs4 import BeautifulSoup   

class Driver():
    # url = 'https://www.formula1.com'
    # name = ''
    # team = ''
    # country = ''
    # podiums = ''
    # points = ''
    # grands_prix_entered = ''
    # world_championships = ''
    # highest_race_finish = ''
    # highest_grid_position = ''
    # date_of_birth = ''
    # place_of_birth = ''

    def __init__(self, link):
        self.url = 'https://www.formula1.com' + link
        self.name = ''
        self.team = ''
        self.country = ''
        self.podiums = ''
        self.points = ''
        self.grands_prix_entered = ''
        self.world_championships = ''
        self.highest_race_finish = ''
        self.highest_grid_position = ''
        self.date_of_birth = ''
        self.place_of_birth = ''


    def crawl_process(self):
        response = requests.get(self.url)
        driver_data_list = list()
        if response.status_code == 200:
            try:
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content)
                    driver_data_list.append(soup.find('h1', class_ = 'driver-name').text.strip())
                    table = soup.find('table', class_ = 'stat-list')
                    driver_datas = table.find_all('td')
                    for element in driver_datas:
                        driver_data_list.append(element.text.strip())
                    self.name = driver_data_list[0]
                    self.team = driver_data_list[1]
                    self.country = driver_data_list[2]
                    self.podiums = driver_data_list[3]
                    self.points = driver_data_list[4]
                    self.grands_prix_entered = driver_data_list[5]
                    self.world_championships = driver_data_list[6]
                    self.highest_race_finish = driver_data_list[7]
                    self.highest_grid_position = driver_data_list[8]
                    self.date_of_birth = driver_data_list[9]
                    self.place_of_birth = driver_data_list[10]
            except Exception as e:
                # Code to handle the exception
                self.name = 'ERROR DATA'



    def __str__(self):
        return f"Name: {self.name}, Team: {self.team}"
    
    def data_storage(self):
        return {'name': self.name, 'team': self.team, 'country': self.country, 'podiums': self.podiums, 'points': self.points, "grands_prix_entered": self.grands_prix_entered, 
                'world_championships':self.world_championships, 'highest_race_finish': self.highest_race_finish, 'highest_grid_position': self.highest_grid_position,
                'date_of_birth': self.date_of_birth, 'place_of_birth': self.place_of_birth}