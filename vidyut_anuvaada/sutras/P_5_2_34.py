# Sutra प.5.2.34: उपाधिभ्यां त्यकन्नासन्नारूढयोः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — upADiByAM tyakannAsannArUQayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.34"
SUTRA_TEXT = "उपाधिभ्यां त्यकन्नासन्नारूढयोः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — upADiByAM tyakannAsannArUQayoH"


class Sutra5234:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.34: अग्निः'),
		('रामः', '', 'प.5.2.34: रामः'),
		('सीता', '', 'प.5.2.34: सीता'),
	]

