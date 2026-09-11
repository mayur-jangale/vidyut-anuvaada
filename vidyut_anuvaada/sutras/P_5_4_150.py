# Sutra प.5.4.150: सुहृद्दुर्हृदौ मित्रामित्रयोः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — suhfddurhfdO mitrAmitrayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.150"
SUTRA_TEXT = "सुहृद्दुर्हृदौ मित्रामित्रयोः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — suhfddurhfdO mitrAmitrayoH"


class Sutra54150:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.150: अग्निः'),
		('रामः', '', 'प.5.4.150: रामः'),
		('सीता', '', 'प.5.4.150: सीता'),
	]

