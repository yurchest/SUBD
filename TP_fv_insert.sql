INSERT INTO Tp_fv(codvuz, z2, z3, numworks)
SELECT codvuz, z2, SUM(f18), COUNT(*)
FROM Tp_nir 
WHERE codvuz = Tp_nir.codvuz
GROUP BY codvuz;
