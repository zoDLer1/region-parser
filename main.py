import requests
from bs4 import BeautifulSoup
from region import Region, Docx_Regions
from configuration import OUTPUT_REGIONS_FLAGS_FILENAME, OUTPUT_REGIONS_INFO_FILENAME
import os
import shutil


class Parser:

    DOMAIN = 'https://geo.koltyrin.ru/'


    PAGES = {
        'regions' : 'regiony_rossii.php',
        'region': 'region_rossii.php'
    }


    def create_temp(self):
        os.makedirs("temp", exist_ok=True)

    def clear_temp(self):
        shutil.rmtree('temp')

    def __init__(self) -> None:
        self.session = requests.Session()
        self.flags = Docx_Regions()
        self.info = Docx_Regions()

    @classmethod
    def url(cls, key):
        return cls.DOMAIN + cls.PAGES[key]

    def parse_regions(self):
        self.create_temp()
        response = self.session.get(self.url('regions'))
        parser = BeautifulSoup(response.text, 'html.parser')
        table = parser.find('table')
        regions = table.find_all('tr')[1:]

        print('| ' + 'Название', 'Адм. единица', 'Рег. центр', 'Площаль', 'Насиление' + ' |', sep=' | ')
        print('-' * 62)
        for region in regions:
            fields = region.find_all('td', recursive=False)
            region_url = fields[0].a['href']
            self.parse_region(region_url[region_url.find('=')+1:])
            region = Region(*map(lambda item: item.get_text(), fields), region_url=region_url)

            name, status, center, square, population, *_ = map(lambda item: item.get_text(), fields)
            print('| ' + name, status, center, square, population + ' |', sep=' | ')

            self.flags.add_region_images(region)
            self.info.add_region_info(region)

        self.flags.save(OUTPUT_REGIONS_FLAGS_FILENAME)
        self.info.save(OUTPUT_REGIONS_INFO_FILENAME)
        self.clear_temp()

    def parse_image(self, url, name):
        response = self.session.get(url)

        with open(f'temp/{name}.png', 'wb') as file:
            file.write(response.content)

    def parse_region(self, region_name):
        response = self.session.get(self.url('region'), params={'region':region_name})
        parser = BeautifulSoup(response.text, 'html.parser')
        flag, emblem = parser.center.find_all('img')
        self.parse_image(self.DOMAIN + flag['src'], 'flag')
        self.parse_image(self.DOMAIN + emblem['src'], 'emblem')







if __name__ == '__main__':
    parser = Parser()
    parser.parse_regions()




