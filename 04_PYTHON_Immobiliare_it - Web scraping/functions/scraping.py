
import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup

#1st function

def scraping_areas_immobiliare(city, ads_type, appartment_type):

    '''
    Return a list of all area names in a city.

    This function get all the area names related to a city from the web site www.immobiliare.it 
    as string and then appends them in a list.

    
    Parameters
    ----------
    city : str
        City to search on the website.

    ads_type : str
        Ads kind to search on the website.
    
    appartment_type : str
        Appartment type to search on the website.


    Return
    ----------
    list
        The list of all the area names related to a city on the web site www.immobiliare.it.

        
    Notes
    ----------
    For the parameter ads_type you should choose the following keyword: rent ('affitto') or sale ('vendita').
    For the parameter appartment_type you should choose the following keyword: houses ('case') or rooms ('stanze').

    '''

    #get the url through the parameters choose
    parameter_1 = city
    parameter_2 = ads_type 
    parameter_3 = appartment_type   
    url_search = "https://www.immobiliare.it/" + parameter_2 + "-" + parameter_3 + "/" + parameter_1 + "/?criterio=rilevanza"

    
    #get the list of area names
    url = url_search
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("ul", class_="nd-stack").find_all("li", class_="nd-stackItem")

    list_temp = []
    for c in results:
        list_temp.append(c.find("a", class_="in-breadcrumb__dropdownLink").text)
    
    #split every element of the list above because they could be an composed by more area names delimited by commas
    list_temp2 = []
    for x in list_temp:
        list_temp2.extend(x.split(","))

    #delete all blanks in first position for each element of the list above
    for i in range(len(list_temp2)):
        list_temp2[i] = list_temp2[i].lstrip()

    return  list_temp2


#2nd function

def scraping_immobiliare(city, ads_type, appartment_type, area):

    '''
    Return a dataframe with real estate ads data about one city area.

    This function get all the real estate ads data related to a city area from the web site www.immobiliare.it 
    and then adds them into a dataframe. Each row rappresent a single real estate ad.
    The dataframe has the following columns:
    - titles --> this is the ad title;
    - city --> this is the city where the appartment is located;
    - area --> this is the area where the appartment is located;
    - prices --> this is the sale price or the rent amount (depend on the ads_type parameter);
    - surface --> this is the surface amount;
    - floor --> this is the floor number;
    - rooms --> this is the number of rooms;
    - bathroom --> this is the number of bathroom.

    
    Parameters
    ----------
    city : str
        City to search on the website.
    
    ads_type : str
        Ads kind to search on the website.
    
    appartment_type : str
        Appartment type to search on the website.
    
    area : str
        Area to search on the website.

        
    Return
    ----------
    dataframe
        The dataframe of all the real estate ads data related to one city area from the web site www.immobiliare.it.

           
    Notes
    ----------
    For the parameter ads_type you should choose the following keyword: rent ('affitto') or sale ('vendita').
    For the parameter appartment_type you should choose the following keyword: houses ('case') or rooms ('stanze').

    '''

    #get the url through the parameters choose
    parameter_1 = city
    parameter_2 = ads_type 
    parameter_3 = appartment_type
    parameter_4 = area
    url_search = "https://www.immobiliare.it/" + parameter_2 + "-" + parameter_3 + "/" + parameter_1 + "/" + parameter_4 + "/?criterio=rilevanza"

    #get the pages number based on the research with the parameters choose
    url = url_search
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    #when the research get '....' as last page number use if otherwise use else
    #this is necessery to get the correct number of pages
    if soup.find("div", class_="in-pagination__list").find_all("div", class_="in-pagination__item hideOnMobile in-pagination__item--disabled") != []:
        results = soup.find("div", class_="in-pagination__list").find_all("div", class_="in-pagination__item hideOnMobile in-pagination__item--disabled")
        n_pages = int(results[-1].text)
    else:
        results = soup.find("div", class_="in-pagination__list").find_all("a")
        n_pages = int(results[-1].text)

    #make a list with every ad id
    id_annunci = []
    for page in range(1,n_pages+1):
        url = url_search + '&pag=' + str(page)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("li", class_="nd-list__item in-realEstateResults__item")
        for id in results: 
            id_annunci.append(id.attrs.get('id'))

        titles = []
        prices = []
        rooms = [] 
        surface = [] 
        bathrooms = []
        floor = []

    #for each ad, get data and then add them to the related list
    for page in range(1,n_pages+1):
        url = url_search + '&pag=' + str(page)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        for ad in id_annunci:
            results = soup.find(id=ad)
            if type(results) != type(None):
                try:
                    results_titles = results.find("a", class_="in-card__title")
                    titles.append(results_titles.text.strip())
                except:
                    titles.append(None)
                try:
                    results_prices = results.find("li", class_="nd-list__item in-feat__item in-feat__item--main in-realEstateListCard__features--main")
                    prices.append(results_prices.text.strip())
                except:
                    prices.append(None)
                try:
                    results_surface = results.find("li", {"aria-label" : "superficie"})
                    surface.append(results_surface.text.strip())
                except:
                    surface.append(None)
                try:
                    results_rooms = results.find("li", {"aria-label" : ["locale", "locali"]})
                    rooms.append(results_rooms.text.strip())
                except:
                    rooms.append(None)
                try:
                    results_bathrooms = results.find("li", {"aria-label" : ["bagno", "bagni"]})
                    bathrooms.append(results_bathrooms.text.strip())
                except:
                    bathrooms.append(None)
                try:
                    results_floor = results.find("li", {"aria-label" : ["piano", "piani"]})
                    floor.append(results_floor.text.strip())
                except:
                    floor.append(None)
            else:
                continue         
    
    #make a dataframe with the lists above
    df_tmp = pd.DataFrame({
                                    'title': titles, 
                                     'city': city,
                                     'area': area,
                                     'price': prices,
                                     'surface': surface,
                                     'floor': floor,
                                     'rooms': rooms,
                                     'bathrooms': bathrooms
                                     })

    return  df_tmp

#3rd function

def city_dataframe(city, ads_type, appartment_type):

    '''
    Return a dataframe with real estate ads data about all city areas.

    This function uses the first function to get a list of all city area names from the web site www.immobiliare.it.
    Then it uses the second function with a 'for cycle' to get a dataframe for each city area name in the list above
    and at last concatenates them.  
    The dataframe has the following columns:
    - titles --> this is the ad title;
    - city --> this is the city where the appartment is located;
    - area --> this is the area where the appartment is located;
    - prices --> this is the sale price or the rent amount (depend on the ads_type parameter);
    - surface --> this is the surface amount;
    - floor --> this is the floor number;
    - rooms --> this is the number of rooms;
    - bathroom --> this is the number of bathroom.

  
    Parameters
    ----------
    city : str
        City to search on the website.
    
    ads_type : str
        Ads kind to search on the website.
    
    appartment_type : str
        Appartment type to search on the website.
    
        
    Return
    ----------
    dataframe
        The dataframe of all the real estate ads data related to all city areas from the web site www.immobiliare.it.

           
    Notes
    ----------
    For the parameter ads_type you should choose the following keyword: rent ('affitto') or sale ('vendita').
    For the parameter appartment_type you should choose the following keyword: houses ('case') or rooms ('stanze').

    '''
    parameter_1 = city
    parameter_2 = ads_type 
    parameter_3 = appartment_type
    
    df_tmp_raw = pd.DataFrame()

    # make a list with all area names of a city
    list_areas = scraping_areas_immobiliare(parameter_1, parameter_2, parameter_3) 
 
    # make a df for each area and then concatenate it to df_tmp_raw
    for c in list_areas:
        try:
            df_tmp = scraping_immobiliare(parameter_1, parameter_2, parameter_3, c)
            df_tmp_raw = pd.concat([df_tmp, df_tmp_raw])
        except:
            continue

    df_tmp_raw.index = pd.RangeIndex(len(df_tmp_raw.index)) # re-index df to avoid duplicates in the index

    return df_tmp_raw