# Sutra प.5.3.74: कुत्सिते
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kutsite

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.74"
SUTRA_TEXT = "कुत्सिते"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kutsite"


class Sutra5374:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.74: अग्निः'),
		('रामः', '', 'प.5.3.74: रामः'),
		('सीता', '', 'प.5.3.74: सीता'),
	]

