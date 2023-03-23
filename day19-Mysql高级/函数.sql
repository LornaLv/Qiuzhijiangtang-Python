SELECT ASCII('A');
SELECT ASCII('a');

SELECT CONCAT(1,2,3,'abc',2222);

SELECT LEFT('abcdefhghijklmnopqrstuvwxyz',6);
SELECT RIGHT('abcdefhghijklmnopqrstuvwxyz',6);
SELECT SUBSTRING('abcdefhghijklmnopqrstuvwxyz',6,10);

SELECT TRIM('abcdefhghijklmnopqrstuvwxyz');
SELECT TRIM(LEADING 'x' FROM 'xxxxxxxxabcdefhghijklmnopqrstuvwxyzxxxxxxxxxx');
SELECT TRIM(BOTH 'x' FROM 'xxxxxxxxxabcdefhghijklmnopqrstuvwxyzxxxxxxxxxx');
SELECT TRIM(TRAILING 'x' FROM 'xxxxxxxxabcdefhghijklmnopqrstuvwxyzxxxxxxxxx');

SELECT REPLACE('abc123','123','def');
SELECT LOWER('aBcD');