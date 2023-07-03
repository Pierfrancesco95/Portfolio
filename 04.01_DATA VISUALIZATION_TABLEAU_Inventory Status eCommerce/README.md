# Inventory Status - The Look eCommerce

Among the public datasets of BigQuery on Google Cloud Platform I chose to analyze the database "The look eCommerce" (dataset ID: bigquery-public-data.thelook_ecommerce) extracted with SQL queries.

After an initial analysis aimed at understanding the relationships between the tables, I created an ER Diagram to represent these relationships. Based on this, I extracted the inventory data in CSV format using a query.

After exploring and cleaning the data using Python, I saved a new version of the dataset in CSV format which I used to represent the insights with Tableau making two dashboards.

From here begins the analysis on the status of the warehouse.

The above working files are attached in the "Working Files" folder.

Below is a brief summary that can help in reading the dashboards.

### 1) "Inventory Analysis 2022" Dashboard
- Main indicators of inventories (valued at cost) which show us how they moved during the year;
- Note that the dashboard shows information for 25k different products;
- Monthly trend of purchases and sales in the three-year period 2020-2022 shows us how sales increase more than purchases on a monthly basis;
- We note that the purchases are, in terms of quantity, almost equal to the initial inventories, this is due to the fact that we are forced to make supplies of products that we do not have in stock in order to finalize the sales. This is reflected in very high closing inventories;
- Let's go down to a greater level of analysis detail by calculating the inventory turn over and comparing the results between the products in the next dashboard.

### 2) Inventory Turn Over 2022 Dashboard
- We have an overall inventory Turn Over of 0.33;
- This result is given by the ratio between COGS (Cost of goods sold) and AVG Inventory (ie, opening inventories plus closing inventories, divided by 2);
- The same overall result affects the various distribution centers in a similar way;
- Analyzing the best and worst products in terms of inventory turn over, we notice that we have a maximum of 4 and a minimum of 0.05;
- Observing the distribution of the Inventory Turn Over values of each product, we notice that most of the products have a result between 0.15 and 0.45;

### CONCLUSIONS:

- Inventory turn over indicates how fast inventories are "turning over" in the warehouse. The higher this indicator is, the faster the sales are (and it's generally good for the business). The lower it is, the more there are weak sales and/or excess inventories;

- Having stationary materials in stock represents a cost (both in terms of management and opportunity cost for lost sales);

- In a sector such as clothing, subject to factors such as fashion that denote a strong seasonality, it is necessary to have a high inventory turnover in order to be competitive and mitigate the risk of unsold products and obsolescence;

- To avoid this risk, you can act in two directions:

a) review product procurement policies based on sales forecasts;

b) boost sales through discount strategies in order to "empty" the warehouse.


