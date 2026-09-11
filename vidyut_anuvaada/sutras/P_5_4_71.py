# Sutra प.5.4.71: नञस्तत्पुरुषात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — naYastatpuruzAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.71"
SUTRA_TEXT = "नञस्तत्पुरुषात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — naYastatpuruzAt"


class Sutra5471:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.71: अग्निः'),
		('रामः', '', 'प.5.4.71: रामः'),
		('सीता', '', 'प.5.4.71: सीता'),
	]

