/*
NIM            : 23102010093
Nama Panggilan : William
*/

-- Data used is in https://www.w3schools.com/sql/trysqlserver.asp?filename=trysql_select_all 

-- If Sales is Quantity x Price, make an SQL Server script which produces a table of Top 5 Sales in January 1997 which shows:
-- The Name of the supplier company, the sales of the company, the proportion of sales within America and europe.



-- Soal 1
-- Pembuatan CTE COUNTRIES dengan kolom COUNTRY dan CONTINENT untuk menyimpan data Continent customer
WITH
    COUNTRIES
AS
    (
    SELECT
        Country AS COUNTRY,
        CASE 
            WHEN Country IN ('Argentina', 'Brazil', 'Canada', 'Mexico', 'USA', 'Venezuela') THEN 'America'
            WHEN Country IN ('Japan', 'Singapore') THEN 'Asia'
            WHEN Country IN ('Austria', 'Belgium', 'Denmark', 'Finland', 'France', 'Germany', 'Ireland', 'Italy', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Spain', 'Sweden', 'Switzerland', 'UK') THEN 'Europe'
            WHEN Country = 'Australia' THEN 'Australia'
            ELSE NULL
        END AS CONTINENT
    FROM
        (
        SELECT 
            Country 
        FROM 
            Customers
        UNION
        SELECT 
            Country 
        FROM 
            Suppliers
        ) AS CTR
    ),

-- Pembuatan CTE SUPP_SALES dengan kolom SupplierName dari tabel Suppliers, TOTAL_SALES dari perkalian Quantity dan Price dan America_Sales, Europe_Sales, Asia_Sales, Australia_Sales dari perkalian Quantity dan Price berdasarkan Continent
-- Langsung dengan pengambilan top 5 Supplier
    SUPP_SALES
AS
(
    SELECT TOP 5
        Suppliers.SupplierName,
        SUM(OrderDetails.Quantity * Products.Price) AS TOTAL_SALES,
        SUM(CASE WHEN COUNTRIES.CONTINENT = 'America' THEN OrderDetails.Quantity * Products.Price ELSE 0 END) AS America_Sales,
        SUM(CASE WHEN COUNTRIES.CONTINENT = 'Europe' THEN OrderDetails.Quantity * Products.Price ELSE 0 END) AS Europe_Sales,
        SUM(CASE WHEN COUNTRIES.CONTINENT = 'Asia' THEN OrderDetails.Quantity * Products.Price ELSE 0 END) AS Asia_Sales,
        SUM(CASE WHEN COUNTRIES.CONTINENT = 'Australia' THEN OrderDetails.Quantity * Products.Price ELSE 0 END) AS Australia_Sales
    FROM
        Suppliers

-- Penggabungan Tabel Suppliers dengan Products, OrderDetails, Orders, Customers, dan COUNTRIES
    INNER JOIN Products ON Suppliers.SupplierID = Products.SupplierID
    INNER JOIN OrderDetails ON OrderDetails.ProductID = Products.ProductID
    INNER JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
    INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
    INNER JOIN COUNTRIES ON Customers.Country = COUNTRIES.COUNTRY

-- Filtering berdasarkan waktu order dan pengelompokan berdasarkan SupplierName, serta pengurutan berdasarkan TOTAL_SALES
    WHERE
        MONTH(Orders.OrderDate) = 1
        AND YEAR(Orders.OrderDate) = 1997
    GROUP BY
        Suppliers.SupplierName

    ORDER BY TOTAL_SALES DESC
)
-- Pengambilan nama Supplier bersama dengan Totals_Sales, dan perecentage sales yang didapatkan dari pembagian sales continent dan total sales
SELECT
    SUPP_SALES.SupplierName AS Supplier_Name,
    FORMAT(TOTAL_SALES, 'N0', 'en-us') AS Total_Sales,
    FORMAT(((America_Sales)/TOTAL_SALES),'P1') AS Percentage_America_Sales,
    FORMAT(((Europe_Sales)/TOTAL_SALES),'P1') AS Percentage_Europe_Sales
FROM
    SUPP_SALES




