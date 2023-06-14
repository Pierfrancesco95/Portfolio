
import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup

# questa funzione ritorna la lista di tutte le zone relative ad una città, richiede come argomenti:
# la città ed il tipo di annuncio (affitto/vendita)

def scraping_zone_immobiliare(city, rent_sale):
    
    città = city
    tipo_annuncio = rent_sale  # utilizzare come keyword "vendita" oppure "affitto"
    url_search = "https://www.immobiliare.it/" + tipo_annuncio + "-case/" + città + "/?criterio=rilevanza"

    #otteniamo la lista delle zone dalla ricerca prefissata
    url = url_search
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("ul", class_="nd-stack").find_all("li", class_="nd-stackItem")

    list_temp = []
    for c in results:
        list_temp.append(c.find("a", class_="in-breadcrumb__dropdownLink").text)
    
    
    #separiamo ogni singolo elemento della lista di sopra che è in realtà composto da più zone separata da virgola

    list_temp2 = []
    for x in list_temp:
        list_temp2.extend(x.split(","))

    #eliminiamo lo spazio che si trova in prima posizione per ogni elemento della lista sopra

    for i in range(len(list_temp2)):
        list_temp2[i] = list_temp2[i].lstrip()

    return  list_temp2


# questa funzione ritorna un dataframe con i dati degli annunci relativi una specifica zone di una città, richiede come argomenti: 
# la città, la zone ed il tipo di annuncio (affitto/vendita)

def scraping_immobiliare(city, zone, rent_sale):
    #fissiamo la città e la zona oggetto di ricerca per case in vendita
    città = city
    zona = zone
    tipo_annuncio = rent_sale  # utilizzare come keyword "vendita" oppure "affitto"
    url_search = "https://www.immobiliare.it/" + tipo_annuncio + "-case/" + città + "/" + zona + "/?criterio=rilevanza"

    #otteniamo il numero di pagine risultati dalla ricerca prefissata
    url = url_search
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    #quando la ricerca produce un ultimo numero di pagine che è successivo a '...' prendi il valore con if, altrimenti prendi il valore con else
    #serve a prendere il numero di pagine correttamente
    if soup.find("div", class_="in-pagination__list").find_all("div", class_="in-pagination__item hideOnMobile in-pagination__item--disabled") != []:
        results = soup.find("div", class_="in-pagination__list").find_all("div", class_="in-pagination__item hideOnMobile in-pagination__item--disabled")
        n_pages = int(results[-1].text)
    else:
        results = soup.find("div", class_="in-pagination__list").find_all("a")
        n_pages = int(results[-1].text)

    #Creiamo una lista contente l'id di ogni annuncio
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
        locali = []
        superficie = []
        bagni = []
        piano = []

    #per ogni annuncio, estraggo i dati e poi li aggiugno alla rispettiva lista
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
                    results_superficie = results.find("li", {"aria-label" : "superficie"})
                    superficie.append(results_superficie.text.strip())
                except:
                    superficie.append(None)
                try:
                    results_locali = results.find("li", {"aria-label" : ["locale", "locali"]})
                    locali.append(results_locali.text.strip())
                except:
                    locali.append(None)
                try:
                    results_bagni = results.find("li", {"aria-label" : ["bagno", "bagni"]})
                    bagni.append(results_bagni.text.strip())
                except:
                    bagni.append(None)
                try:
                    results_piano = results.find("li", {"aria-label" : ["piano", "piani"]})
                    piano.append(results_piano.text.strip())
                except:
                    piano.append(None)
            else:
                continue         
    
    df_tmp = pd.DataFrame({
                                    'title': titles, #titolo annuncio
                                     'città': città,
                                     'zona': zona,
                                     'prezzo': prices,
                                     'superfice': superficie,
                                     'piani': piano,
                                     'locali': locali,
                                     'bagni': bagni
                                     })

    return  df_tmp


# questa funziona ritorna un dataframe con i dati di tutti gli annunci di una città, richiede come argomenti:
# la città ed il tipo di annuncio (affitto/vendita)
# utilizza le due funzioni precedenti

def city_dataframe(city, rent_sale):
    città = city
    tipo_annuncio = rent_sale  # utilizzare come keyword "vendita" oppure "affitto"
    df_tmp_raw = pd.DataFrame()

    list_zone = scraping_zone_immobiliare(città, tipo_annuncio ) #creo la lista di tutte le zone di una città

    for c in list_zone:
        try:
            df_tmp = scraping_immobiliare(città, c, tipo_annuncio)
            df_tmp_raw = pd.concat([df_tmp_raw, df_tmp])
        except:
            continue

    df_tmp_raw.index = pd.RangeIndex(len(df_tmp_raw.index)) # re-index df per evitare duplicati nell'indice

    return df_tmp_raw