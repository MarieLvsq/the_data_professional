Use bus_depots;
Select bdno, bdname from busdriver d where bdsalary <= 1800;
Select bdno, bdname from busdriver where bdname LIKE "J%";
Select bdno, bdname from busdriver where bdsalary between 2000 and 4000;
SELECT regno, model from bus where tno =2 and dno != 101;
SELECT regno, model from bus where model LIKE "Volvo%" or model LIKE "Mercedes%";
SELECT DISTINCT dno FROM bus;
SELECT cno, cname FROM cleaner 
INNER JOIN depot ON cleaner.dno = depot.dno;
SELECT DISTINCT busdriver.bdno, busdriver.bdname, tdescript FROM busdriver 
LEFT JOIN training ON training.bdno = busdriver.bdno
RIGHT JOIN bustype ON training.tno = bustype.tno;
SELECT c.cno, c.cname, c.dno, b.regno, bt.tdescript FROM cleaner c
LEFT JOIN bus b ON b.cno = c.cno
RIGHT JOIN bustype bt ON bt.tno = b.tno;
SELECT c.cno, c.cname, c.dno, b.regno, bt.tdescript FROM cleaner c
LEFT JOIN depot d ON c.dno = d.dno
LEFT JOIN bus b ON c.cno = b.cno
LEFT JOIN bustype bt ON b.tno = bt.tno;
