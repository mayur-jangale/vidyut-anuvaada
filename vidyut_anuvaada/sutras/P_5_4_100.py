# Sutra प.5.4.100: अर्धाच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — arDAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.100"
SUTRA_TEXT = "अर्धाच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — arDAcca"


class Sutra54100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.100: अग्निः'),
		('रामः', '', 'प.5.4.100: रामः'),
		('सीता', '', 'प.5.4.100: सीता'),
	]

