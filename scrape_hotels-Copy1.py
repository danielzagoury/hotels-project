#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


class hotel:
    def __init__(self,name_of_the_hotel=None,rate_of_the_hotel=None,location_rating=None,comfort=None,staff=None,desk_all_time=None,rate_of_facilities=None,swimming_pool=None,bar=None,wifi=None,value_for_money=None,
                 parking=None,Elevator=None,Cleanliness=None,Babysitting_Child_services=None,Sauna=None,pets=None,Wheelchair_accessible=None,safe=None):
        self.name_of_the_hotel = name_of_the_hotel
        self.rate_of_the_hotel = rate_of_the_hotel
        self.location_rating = location_rating
        self.comfort = comfort
        self.staff = staff
        self.desk_all_time = desk_all_time
        self.rate_of_facilities = rate_of_facilities
        self.swimming_pool = swimming_pool
        self.bar = bar
        self.wifi = wifi
        self.value_for_money = value_for_money
        self.parking = parking
        self.Elevator = Elevator
        self.Cleanliness = Cleanliness
        self.Babysitting_Child_services = Babysitting_Child_services
        self.Sauna = Sauna
        self.pets = pets
        self.Wheelchair_accessible = Wheelchair_accessible
        self.safe = safe


# In[ ]:


def get_links(url):
    links = []
    driver = webdriver.Chrome()
    driver.get(url)
    hotels = driver.find_elements(By.CLASS_NAME, 'e13098a59f')
    for hotel in hotels:
        link = hotel.get_attribute("href")
        links.append(link)
    return links


# In[ ]:


def next_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    link = driver.find_element(By.XPATH,'.//*[@id="search_results_table"]/div[2]/div/div/div/div[4]/div[2]/nav/div/div[3]/button')
    link.click()
    driver.implicitly_wait(5)
    return driver.current_url


# In[ ]:


def scrape_hotel_details(url):
    html = requests.get(url).content
    data = BeautifulSoup(html, 'html.parser')
    all_content = data.find(id="hotelTmpl")
    h=hotel()
    # name
    try:
        name = all_content.find(attrs={"class": "d2fee87262 pp-header__title"}).text
        h.name_of_the_hotel=name
    except:
        pass
    try:
        rates = all_content.find_all(attrs={"class": "ee746850b6 b8eef6afe1"})
        for i in range(len(rates)):
            rates[i] = rates[i].text
    except:
        pass
    # get the rate of the hotel
    try:
        rate = all_content.find(attrs={"class": "b5cd09854e d10a6220b4"}).text
        h.rate_of_the_hotel=rate
    except:
        pass
    # if 24\7 front desk
    try:
        desk = all_content.find_all("div", attrs={"class": "db29ecfbe2 c21a2f2d97 fe87d598e8"})
        for i in range(len(desk)):
            desk[i] = desk[i].text
        if "24-hour front desk" in desk:
            desk = 1
        else:
            desk = 0
        h.desk_all_time=desk
    except:
        pass
    # get the rates of hotel
    try:
        location_rating = rates[5]
        h.location_rating=location_rating
    except:
        pass
    try:
        value_for_money = rates[4]
        h.value_for_money=value_for_money
    except:
        pass
    try:
        Cleanliness = rates[2]
        h.Cleanliness=Cleanliness
    except:
        pass
    try:
        comfort = rates[3]
        h.comfort=comfort
    except:
        pass
    try:
        staff = rates[0]
        h.staff=staff
    except:
        pass
    try:
        rate_of_facilities = rates[1]
        h.rate_of_facilities=rate_of_facilities
    except:
        pass
    # facilities
    try:
        facilities = all_content.find_all(attrs={"class": "db29ecfbe2"})
        for i in range(len(facilities)):
            facilities[i] = facilities[i].text.strip("\n")
        facilities2 = all_content.find_all(attrs={"class": "bui-list__description"})
        for i in range(len(facilities2)):
            facilities2[i] = facilities2[i].text.strip("\n")
        facilities_fusion = facilities + facilities2
    except:
        pass
    # wifi
    try:
        if any("WiFi is available" in s for s in facilities_fusion):
            wifi = 1
        else:
            wifi = 0
        h.wifi=wifi
    except:
        pass
    # pool
    try:
        if any(" pool " in s for s in facilities_fusion):
            swimming_pool = 1
        else:
            swimming_pool = 0
        h.swimming_pool=swimming_pool
    except:
        pass
    # bar
    try:
        if any("Bar" in s for s in facilities_fusion):
            bar = 1
        else:
            bar = 0
        h.bar=bar
    except:
        pass
    # safe
    try:
        if (any("Safe" in s for s in facilities_fusion ) or any("Safety deposit box" in s for s in facilities_fusion )):
            safe = 1
        else:
            safe = 0
        h.safe=safe
    except:
        pass
    # Elevator
    try:
        if any("Elevator" in s for s in facilities_fusion) or any("lift" in s for s in facilities_fusion):
            Elevator = 1
        else:
            Elevator = 0
        h.Elevator=Elevator
    except:
        pass
    # Sauna
    try:
        if any("Sauna" in s for s in facilities_fusion):
            Sauna = 1
        else:
            Sauna = 0
        h.Sauna=Sauna
    except:
        pass
    # Parking
    try:
        if any("Parking" in s for s in facilities_fusion):
            parking = 1
        else:
            parking = 0
        h.parking=parking
    except:
        pass
    # Pets
    try:
        if any("Pets" in s for s in facilities_fusion):
            pets = 1
        else:
            pets = 0
        h.pets=pets
    except:
        pass
    # Wheelchair accessible
    try:
        if any("Wheelchair" in s for s in facilities_fusion):
            Wheelchair_accessible = 1
        else:
            Wheelchair_accessible = 0
        h.Wheelchair_accessible=Wheelchair_accessible
    except:
        pass
    # Babysitting Child services
    try:
        if any("Babysitting" in s for s in facilities_fusion):
            Babysitting_Child_services = 1
        else:
            Babysitting_Child_services = 0
        h.Babysitting_Child_services=Babysitting_Child_services
    except:
        pass

    return h


# In[ ]:


url_london='https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaGqIAQGYATG4AQfIAQzYAQHoAQH4AQKIAgGoAgO4AqyGhp4GwAIB0gIkZTkwNWM4MDItM2UyYi00YWY4LTk2MTMtMjNhNjQ3ZDFmZmMz2AIF4AIB&sid=a44a6258ce73fd2a52d0d5bed29c1969&aid=304142&checkin=2023-11-20&checkout=2023-11-24&dest_id=-2601889&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&offset=0'
all_links_london =[]
url_rome='https://www.booking.com/searchresults.en-gb.html?ss=Rome%2C+Lazio%2C+Italy&ssne=Roma&ssne_untouched=Roma&efdco=1&label=mexico%2Froma-7zYHlv0p30c84HApzOmk1AS541207420039%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1929631084068%3Akwd-1006826128%3Alp1008004%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0&sid=a44a6258ce73fd2a52d0d5bed29c1969&aid=1610684&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-126693&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=e3bb63f5df3e019c&ac_meta=GhBlM2JiNjNmNWRmM2UwMTljIAAoATICZW46AlJvQABKAFAA&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
all_links_rome =[]
url_Barcelona='https://www.booking.com/searchresults.en-gb.html?ss=Barcelona%2C+Catalonia%2C+Spain&ssne=Rome&ssne_untouched=Rome&efdco=1&label=mexico%2Froma-7zYHlv0p30c84HApzOmk1AS541207420039%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1929631084068%3Akwd-1006826128%3Alp1008004%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0&sid=a44a6258ce73fd2a52d0d5bed29c1969&aid=1610684&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-372490&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=6905645bc4df0499&ac_meta=GhA2OTA1NjQ1YmM0ZGYwNDk5IAAoATICZW46A2JhckAASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
all_links_Barcelona =[]

cities = []
names = []
rates = []
comfort= []
location_rates= []
staff= []
desk= []
rate_of_facilities= []
swimming_pool= []
bar= []
wifi= []
value_for_money= []
parking= []
Elevator= []
Cleanliness= []
Babysitting_Child_services= []
Sauna= []
pets= []
Wheelchair_accessible= []
safe= []
for i in range(39):
    all_links_london += get_links(url_london)
    url_london = next_page(url_london)
all_links_london += get_links(url_london)
for i in range(39):
    all_links_rome += get_links(url_rome)
    url_rome = next_page(url_rome)
all_links_rome += get_links(url_rome)
for i in range(39):
    all_links_Barcelona += get_links(url_Barcelona)
    url_Barcelona = next_page(url_Barcelona)
all_links_Barcelona += get_links(url_Barcelona)
count=0
for link in all_links_london:
    hotle = scrape_hotel_details(link)
    names.append(hotle.name_of_the_hotel)
    rates.append(hotle.rate_of_the_hotel)
    location_rates.append(hotle.location_rating)
    comfort.append(hotle.comfort)
    staff.append(hotle.staff)
    desk.append(hotle.desk_all_time)
    rate_of_facilities.append(hotle.rate_of_facilities)
    swimming_pool.append(hotle.swimming_pool)
    bar.append(hotle.bar)
    wifi.append(hotle.wifi)
    value_for_money.append(hotle.value_for_money)
    parking.append(hotle.parking)
    Elevator.append(hotle.Elevator)
    Cleanliness.append(hotle.Cleanliness)
    Babysitting_Child_services.append(hotle.Babysitting_Child_services)
    Sauna.append(hotle.Sauna)
    pets.append(hotle.pets)
    Wheelchair_accessible.append(hotle.Wheelchair_accessible)
    safe.append(hotle.safe)
    hotle.city = "London"
    cities.append(hotle.city)


for link in all_links_rome:
    hotle = scrape_hotel_details(link)
    names.append(hotle.name_of_the_hotel)
    rates.append(hotle.rate_of_the_hotel)
    location_rates.append(hotle.location_rating)
    comfort.append(hotle.comfort)
    staff.append(hotle.staff)
    desk.append(hotle.desk_all_time)
    rate_of_facilities.append(hotle.rate_of_facilities)
    swimming_pool.append(hotle.swimming_pool)
    bar.append(hotle.bar)
    wifi.append(hotle.wifi)
    value_for_money.append(hotle.value_for_money)
    parking.append(hotle.parking)
    Elevator.append(hotle.Elevator)
    Cleanliness.append(hotle.Cleanliness)
    Babysitting_Child_services.append(hotle.Babysitting_Child_services)
    Sauna.append(hotle.Sauna)
    pets.append(hotle.pets)
    Wheelchair_accessible.append(hotle.Wheelchair_accessible)
    safe.append(hotle.safe)
    hotle.city = "Rome"
    cities.append(hotle.city)

for link in all_links_Barcelona:
    hotle = scrape_hotel_details(link)
    names.append(hotle.name_of_the_hotel)
    rates.append(hotle.rate_of_the_hotel)
    location_rates.append(hotle.location_rating)
    comfort.append(hotle.comfort)
    staff.append(hotle.staff)
    desk.append(hotle.desk_all_time)
    rate_of_facilities.append(hotle.rate_of_facilities)
    swimming_pool.append(hotle.swimming_pool)
    bar.append(hotle.bar)
    wifi.append(hotle.wifi)
    value_for_money.append(hotle.value_for_money)
    parking.append(hotle.parking)
    Elevator.append(hotle.Elevator)
    Cleanliness.append(hotle.Cleanliness)
    Babysitting_Child_services.append(hotle.Babysitting_Child_services)
    Sauna.append(hotle.Sauna)
    pets.append(hotle.pets)
    Wheelchair_accessible.append(hotle.Wheelchair_accessible)
    safe.append(hotle.safe)
    hotle.city = "Barcelona"
    cities.append(hotle.city)


# In[ ]:


hotels_df = pd.DataFrame({"name": names, "rate_of_the_hotel": rates, "location_rating": location_rates, "comfort": comfort, "staff": staff, "desk_24/7": desk, "rate_of_facilities": rate_of_facilities, "swimming_pool": swimming_pool, "bar": bar, "wifi": wifi, "value_for_money": value_for_money, "parking": parking, "Elevator": Elevator, "Cleanliness": Cleanliness, "Babysitting_Child_services": Babysitting_Child_services, "Sauna": Sauna, "pets": pets, "Wheelchair_accessible": Wheelchair_accessible, "safe": safe,"city":cities})
compression_opts = dict(method='zip',archive_name='hotels_df.csv')
hotels_df.to_csv('hotels_data.zip', index=False,compression=compression_opts)

