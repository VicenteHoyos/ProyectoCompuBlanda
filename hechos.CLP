(deftemplate FichaPaciente
	(field Nombre)
	(field Edad)
	(field Peso)
	(field Fumador)
)

(deftemplate Sintomatologia
	(field Sintoma)	
)

(deffacts VariosHechos
	(FichaPaciente
		(Nombre DenimPowell)
		(Edad 17)
		(Peso 70kg)
		(Fumador No)
	)
	(Sintomatologia (Sintoma Tos))
	(Sintomatologia (Sintoma Fiebre))
	(Sintomatologia (Sintoma Vomito))
	(Sintomatologia (Sintoma Deshidratacion))
	(Sintomatologia (Sintoma Tos))
	(Sintomatologia (Sintoma Malestar))
	(Sintomatologia (Sintoma Sarpullido))
	(Sintomatologia (Sintoma Fiebre))
)
