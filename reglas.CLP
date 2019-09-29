(defrule Gripa
	(Sintomatologia (Sintoma Tos))
	(Sintomatologia (Sintoma Fiebre))
	(FichaPaciente
		(Nombre ?Nombre)
		(Edad ?Edad)
		(Peso ?Peso)
		(Fumador ?Fumador)
	)
	=>
	(printout t crlf ?Nombre " tiene gripa y debe tomar acetaminofen" crlf "Ficha Paciente:" crlf "Nombre: " ?Nombre crlf "Edad: " ?Edad crlf "Peso:" ?Peso crlf "Fumador: " ?Fumador crlf  "Sintomas:" crlf "Sintoma 1: Tos" crlf "Sintoma 2: Fiebre" crlf)
)

(defrule Gripa y Diarrea
	(Sintomatologia (Sintoma Vomito))
	(Sintomatologia (Sintoma Deshidratacion))
	(Sintomatologia (Sintoma Tos))
	(Sintomatologia (Sintoma Fiebre))
	(FichaPaciente
		(Nombre ?Nombre)
		(Edad ?Edad)
		(Peso ?Peso)
		(Fumador ?Fumador)
	)
	=>
	(printout t crlf ?Nombre " Tiene diarrea y debe tomar smegta e hidratarse" crlf "Ficha Paciente:" crlf "Nombre: " ?Nombre crlf "Edad: " ?Edad crlf "Peso:" ?Peso crlf "Fumador: " ?Fumador crlf crlf "Sintomas:" crlf "Sintoma 1: Vomito" crlf "Sintoma 2: Deshidratación" crlf "Sintoma 3: Tos" crlf "Sintoma 4: Fiebre" crlf)
)

(defrule Faringitis
	(Sintomatologia (Sintoma Tos))
	(Sintomatologia (Sintoma Malestar))
	(Sintomatologia (Sintoma Vomito))
	(Sintomatologia (Sintoma Deshidratacion))
	(Sintomatologia (Sintoma Fiebre))
	(FichaPaciente
		(Nombre ?Nombre)
		(Edad ?Edad)
		(Peso ?Peso)
		(Fumador ?Fumador)
	)
	=>
	(printout t crlf ?Nombre " Tiene faringitis y necesita una inyeccion de dipirona" crlf "Ficha Paciente:" crlf "Nombre: " ?Nombre crlf "Edad: " ?Edad crlf "Peso:" ?Peso crlf "Fumador: " ?Fumador crlf "Sintomas:" crlf "Sintoma 1: Tos" crlf "Sintoma 2: Malestar" crlf "Sintoma 3: Vomito" crlf "Sintoma 4: Deshidratación" crlf "Sintoma 5: Fiebre" crlf)
)

(defrule Viruela
	(Sintomatologia (Sintoma Sarpullido))
	(Sintomatologia (Sintoma Fiebre))
	(Sintomatologia (Sintoma Tos))
	(Sintomatologia (Sintoma Malestar))
	(Sintomatologia (Sintoma Vomito))
	(Sintomatologia (Sintoma Deshidratacion))
	(FichaPaciente
		(Nombre ?Nombre)
		(Edad ?Edad)
		(Peso ?Peso)
		(Fumador ?Fumador)
	)
	=>
	(printout t crlf ?Nombre " Tiene viruela y debe ser internado" crlf "Ficha Paciente:" crlf "Nombre: " ?Nombre crlf "Edad: " ?Edad crlf "Peso:" ?Peso crlf "Fumador: " ?Fumador crlf  "Sintomas:" crlf "Sintoma 1: Sarpullido" crlf "Sintoma 2: Fiebre" crlf "Sintoma 3: Tos" crlf "Sintoma 4: Malestar" crlf "Sintoma 5: Vomito" crlf "Sintoma 6: Deshidratación" crlf)
)