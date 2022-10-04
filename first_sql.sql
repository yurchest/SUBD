UPDATE	Tp_nir
SET z2 = (SELECT VUZ.z2 FROM VUZ WHERE VUZ.codvuz = TP_nir.codvuz)



INSERT INTO Tp_fv(codvuz, z2, z3, numworks)
SELECT codvuz, z2, SUM(f18), COUNT(*)
FROM Tp_nir 
WHERE codvuz = Tp_nir.codvuz
GROUP BY codvuz;


SELECT SUM(numworks) FROM Tp_fv -- Должно быть 400

SELECT codvuz, rnw, COUNT(*)
FROM Tp_nir
GROUP BY codvuz, rnw
HAVING COUNT(*) > 1;

UPDATE Tp_nir
SET f10 = REPLACE(Tp_nir.f10, ',', ';')