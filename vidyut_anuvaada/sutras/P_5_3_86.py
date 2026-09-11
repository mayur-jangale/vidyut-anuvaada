# Sutra प.5.3.86: ह्रस्वे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — hrasve

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.86"
SUTRA_TEXT = "ह्रस्वे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — hrasve"


class Sutra5386:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.86: अग्निः'),
		('रामः', '', 'प.5.3.86: रामः'),
		('सीता', '', 'प.5.3.86: सीता'),
	]

