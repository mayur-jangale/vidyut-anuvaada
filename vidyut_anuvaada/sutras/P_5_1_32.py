# Sutra प.5.1.32: विंशतिकात् खः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — viMSatikAt KaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.32"
SUTRA_TEXT = "विंशतिकात् खः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — viMSatikAt KaH"


class Sutra5132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.32: अग्निः'),
		('रामः', '', 'प.5.1.32: रामः'),
		('सीता', '', 'प.5.1.32: सीता'),
	]

