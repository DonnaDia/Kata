#Vers 1
select concat_ws(' ', prefix,first,last,suffix) as title from names

#Vers 2
SELECT CONCAT(prefix,' ', first ,' ',last,' ', suffix) as title FROM names