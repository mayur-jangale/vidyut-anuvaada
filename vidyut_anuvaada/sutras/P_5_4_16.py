# Sutra प.5.4.16: विसारिणो मत्स्ये
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — visAriRo matsye

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.16"
SUTRA_TEXT = "विसारिणो मत्स्ये"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — visAriRo matsye"


class Sutra5416:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.16: अग्निः'),
		('रामः', '', 'प.5.4.16: रामः'),
		('सीता', '', 'प.5.4.16: सीता'),
	]

