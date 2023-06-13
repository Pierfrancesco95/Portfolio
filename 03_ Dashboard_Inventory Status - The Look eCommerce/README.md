# Inventory Status - The Look eCommerce

Tra i dataset pubblici di BigQuery su Google Cloud Platform ho scelto di analizzare il database "The look eCommerce" (ID set di dati: bigquery-public-data.thelook_ecommerce) estratto con query SQL.

Dopo una prima analisi volta alla comprensione delle relazioni tra le tabelle, ho realizzato un ER Diagram per rappresentare tali relazioni. Sulla base di ciò, tramite query ho estratto i dati relativi all'inventory.

Dopo aver esplorato e pulito un po' i dati tramite Python, ho salvato una nuova versione csv del dataset che ho utilizzato per svolgere una rappresentazione degli insights tramite Tableau con la creazione di due dashboards.

Da qui inizia l'analisi sullo status del magazzino.

Di seguito un breve summary che può aiutare nella lettura delle dashboards.

### 1) Dashboard "Inventory Analysis 2022"
- Principali indicatori delle rimanenze di magazzino (valorizzati al costo) che ci mostrano come si sono movimentate nell'anno;
- Teniamo presente che la dashboard mostra le informazioni per 25k prodotti differenti;
- Trend mensile degli acquisti e delle vendite nel triennio 2020-2022 ci mostra come le vendite mensilmente aumentino più degli acquisti;
- Notiamo che gli acquisti sono, in termini di quantità, quasi pari alla rimanenze iniziali, questo è dovuto al fatto che siamo costretti a fare approvvigionamenti di prodotti che non abbiamo in magazzino al fine di finalizzare le vendite. Questo si riflette su rimanenze finali molto alte;
- Scendiamo ad un maggior livello di dettaglio dell'analisi calcolando l'inventory turn over e confrontando i risultati tra i prodotti nella prossima dashboard.

### 2) Dashboard "Inventory Turn Over 2022"
- Abbiamo un'inventory Turn Over complessivo pari a 0.33;
- Tale risultato è dato dal rapporto tra COGS (Cost of goods sold) e AVG Inventory (ossia, rimanenze iniziali più rimanenze finali, diviso 2);
- Lo stesso risultato complessivo si ripercuote nei vari centri di distribuzione in maniera similare;
- Analizzando i migliori e peggiori prodotti in termini di inventory turn over, notiamo che abbiamo un massimo di 4 ed un minimo di 0.05;
- Osservando la distribuzione dei valori di Inventory Turn Over di ciascun prodotto, notiamo che la maggior parte dei prodotti ha un risultato tra 0.15 e 0.45;

### CONCLUSIONI:

- L'inventory turn over indica quanto velocemente le rimanenze stanno "ruotando" in magazzino. Più è alto questo indicatore, più le vendite sono veloci (ed è positivo in genere per il business). Più è basso, più ci sono vendite deboli e/o eccesso di rimanenze;

- Avere materie ferme in magazzino rappresenta un costo (sia in termini di gestione che di costo opportunità per le vendite perse);

- In un settore come quello dell'abbigliamento, soggetto a fattori come la moda che denotano una forte stagionalità, è necessario avere un inventory turn over alto per essere competitivi ed mitigare il rischio di invenduto e di obsolescenza dei prodotti;

- Per evitare questo rischio, si può agire in due direzione:

a) rivedere le politiche di approvvigionamento dei prodotti in funzione della previsione delle vendite;

b) spingere sulle vendite tramite strategie di scontistiche al fine di "svuotare" il magazzino.


