# Sutra प.5.4.120: सुप्रातसुश्वसुदिवशारिकुक्षचतुरश्रैणीपदाजपदप्रोष्ठपदाः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — suprAtasuSvasudivaSArikukzacaturaSrERIpadAjapadaprozWapadAH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.120"
SUTRA_TEXT = "सुप्रातसुश्वसुदिवशारिकुक्षचतुरश्रैणीपदाजपदप्रोष्ठपदाः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — suprAtasuSvasudivaSArikukzacaturaSrERIpadAjapadaprozWapadAH"


class Sutra54120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.120: अग्निः'),
		('रामः', '', 'प.5.4.120: रामः'),
		('सीता', '', 'प.5.4.120: सीता'),
	]

