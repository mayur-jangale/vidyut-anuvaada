# Sutra प.5.4.14: णचः स्त्रियामञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — RacaH striyAmaY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.14"
SUTRA_TEXT = "णचः स्त्रियामञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — RacaH striyAmaY"


class Sutra5414:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.14: अग्निः'),
		('रामः', '', 'प.5.4.14: रामः'),
		('सीता', '', 'प.5.4.14: सीता'),
	]

