--roll up
SELECT supplier_key, model_key, branch_key, date_key,SUM(quantity) as Total_income
FROM income_fact
GROUP BY rollup(supplier_key, model_key, branch_key, date_key)
ORDER BY supplier_key, model_key, branch_key, date_key;

--cube
SELECT supplier_key, model_key, branch_key, date_key,SUM(quantity) as Total_income
FROM income_fact
GROUP BY cube(supplier_key, model_key, branch_key, date_key)
ORDER BY supplier_key, model_key, branch_key, date_key;

--pivot
SELECT supplier_key, model_key,SUM(quantity) as Total_income
FROM income_fact
GROUP BY (supplier_key, model_key)
ORDER BY supplier_key, model_key;

--Grouping
SELECT supplier_key, model_key, branch_key,SUM(quantity) as Total_Sale,
    Grouping(supplier_key) as supplier_key_flag,
    Grouping(branch_key) as branch_key_flag,
    Grouping(model_key) as model_key_flag
FROM income_fact
GROUP BY rollup(supplier_key, model_key, branch_key, date_key)
ORDER BY supplier_key, model_key, branch_key, date_key;

--decode operation
SELECT decode(grouping(supplier_key),1, '0', supplier_key) as supplier_key,
   decode(grouping(model_key),1, '0', model_key) as model_key,
   decode(grouping(branch_key),1, '0', branch_key) as branch_key,
   SUM(quantity) as Total_Sale
FROM income_fact
GROUP BY rollup(supplier_key, model_key, branch_key, date_key)
ORDER BY supplier_key, model_key, branch_key, date_key;