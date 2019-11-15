--drop table branches;
CREATE TABLE branches(
branch_key varchar2(50) NOT NULL,
branch_name varchar2(50) NOT NULL,
branch_address varchar2(50) NOT NULL,
country_name varchar2(50) NOT NULL,
Constraint branches_pk Primary key (branch_key)
);


--drop table date_dim;
CREATE TABLE date_dim(
date_key varchar2(50) NOT NULL,
year_val varchar2(50) NOT NULL,
month_val varchar2(50) NOT NULL,
quarter_val varchar2(50) NOT NULL,
day_val varchar2(50) NOT NULL,
Constraint date_dim_pk Primary key (date_key)
);

--drop table Variant;
CREATE TABLE Variant(
variant_key varchar2(50) NOT NULL,
variant_name varchar2(50) NOT NULL,
fuel varchar2(50) NOT NULL,
Constraint variant_pk Primary key (variant_key)
);
--drop table Item;
CREATE TABLE Item(
item_key varchar2(50) NOT NULL,
item_name varchar2(50) NOT NULL,
model_key varchar2(50) NOT NULL,
variant_key varchar2(50) NOT NULL,
Constraint item_pk Primary key (model_key),
Constraint fk_variant Foreign key (variant_key) References Variant(variant_key)
);




--drop table location_dm;
CREATE TABLE location_dm(
location_key varchar2(50) NOT NULL,
region varchar2(50) NOT NULL,
Constraint location_pk Primary key (location_key)
);
--drop table country;
CREATE TABLE country(
country_key varchar2(50) NOT NULL,
country_name varchar2(50) NOT NULL,
Constraint country_pk Primary key (country_key)
);
--drop table supplier;
CREATE TABLE supplier(
supplier_key varchar2(50) NOT NULL,
location_key varchar2(50) NOT NULL,
country_key varchar2(50) NOT NULL,
supplier_name varchar2(50) NOT NULL,
supplier_contact varchar2(50) NOT NULL,
Constraint supplier_pk Primary key (supplier_key),
Constraint fk_location Foreign key (location_key) References location_dm(location_key),
Constraint fk_country Foreign key (country_key) References country(country_key)
);



--drop table income_fact;
CREATE TABLE income_fact (
supplier_key varchar2(50) NOT NULL,
model_key varchar2(50) NOT NULL,
branch_key varchar2(50) NOT NULL,
date_key varchar2(50) NOT NULL,
quantity Number(30) NOT NULL,
income Number(30) NOT NULL,
Constraint fk_supplier Foreign key (supplier_key) References supplier(supplier_key),
Constraint fk_item Foreign key (model_key) References item(model_key),
Constraint fk_branches Foreign key (branch_key) References branches(branch_key),
Constraint fk_date_dim Foreign key (date_key) References date_dim(date_key)
);

