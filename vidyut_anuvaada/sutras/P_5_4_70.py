# Sutra प.5.4.70: किमः क्षेपे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kimaH kzepe

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.70"
SUTRA_TEXT = "किमः क्षेपे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kimaH kzepe"


class Sutra5470:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.70: अग्निः'),
		('रामः', '', 'प.5.4.70: रामः'),
		('सीता', '', 'प.5.4.70: सीता'),
	]

