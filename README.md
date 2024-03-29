# ABDC Dashboard with Dash and SQL - Ongoing

Creating a multi-page web dashboard in which a drug wholesaler can gain an overview of leakage in their Primary Vendor Agreements. 
The dashboard should allow a business user to identify the pharmacy, buying group, and particular products that show the most or least leakage, as well as examine the magnitude of the forgone revenues. 

This an exercise in using **Postgres SQL** to store and query data. I transformed the flat dataset into a normalized database.  Below is the rudimetary database schema I created for this purpose. A normalized database should allow me to practice `JOIN`s queries.


<a href="https://ibb.co/9bSvF9f"><img src="https://i.ibb.co/ByFPXV7/erdplus-diagram.png" alt="erdplus-diagram" border="0"></a>

*Dash* and *Plot.ly* are all new to me, but my skills will improve with time.

**Update June 2019:**
I made my first dashboard view along with a rudimentary layout. My next goal is to get another view and host the app via the Google App Engine.

<a href="https://ibb.co/PDRKhVB"><img src="https://i.ibb.co/WVQZyRS/image.png" alt="image" border="0"></a>
<hr>

<a href="https://ibb.co/ctpTb26"><img src="https://i.ibb.co/WFdKDBk/image.png" alt="image" border="0"></a>
Hue and size represent the dollar amount of sales leakage. Axes in `plotly` are difficult to work with, but I'll add to axis title when I can.
