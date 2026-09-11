# Sutra प.5.2.40: किमिदंभ्यां वो घः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kimidaMByAM vo GaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.40"
SUTRA_TEXT = "किमिदंभ्यां वो घः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kimidaMByAM vo GaH"


class Sutra5240:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.40: अग्निः'),
		('रामः', '', 'प.5.2.40: रामः'),
		('सीता', '', 'प.5.2.40: सीता'),
	]

