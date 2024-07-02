Use bus_depots;
SELECT MAX(bd.bdsalary) AS HigherSalary from busdriver bd;
SELECT MIN(bd.bdsalary) AS LowerSalary from busdriver bd;
SELECT AVG(bd.bdsalary) AS AverageSalary from busdriver bd;
SELECT COUNT(*) AS "Number of bus drivers" FROM busdriver bd ;
SELECT rno, rdescript FROM route
LEFT JOIN depot ON depot.dno = route.dno
WHERE depot.dname LIKE "Holloway";
SELECT * FROM bus where dno IS NULL;
SELECT bd.bdname, bd.bdno FROM busdriver bd
WHERE bd.bdno NOT IN (SELECT a.bdno FROM Ability a);
SELECT depot.dname as "Depot Name", AVG(busdriver.bdsalary) "Average Salary" FROM busdriver 
JOIN depot on depot.dno = busdriver.dno
GROUP BY busdriver.dno;
SELECT d.dname AS "Depot Name", COUNT(*) as "Number of bus drivers" FROM busdriver bd
JOIN depot d ON bd.dno = d.dno
GROUP BY d.dname
HAVING COUNT(bd.dno) > 1;
SELECT c.cname, c.cno, bt.tdescript AS 'bus_type', COUNT(b.regno) AS total_buses from cleaner c
LEFT JOIN bus b ON b.cno = c.cno
LEFT JOIN bustype bt ON b.tno = bt.tno 
WHERE bt.tdescript IN ('midibus', 'double-decker')
GROUP BY c.cname, c.cno, bt.tdescript;
SELECT bd.bdno, bd.bdname AS 'Driver name', r.rno, r.rdescript AS 'Route' FROM busdriver bd
INNER JOIN route r ON r.dno = bd.dno
ORDER BY bd.bdno;
SELECT bd.bdno, bd.bdname AS 'Driver name', r.rno, r.rdescript AS 'Route' FROM busdriver bd
INNER JOIN route r ON r.dno = bd.dno
ORDER BY bd.bdno, r.rdescript;