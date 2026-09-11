# Sutra प.5.4.137: उपमानाच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — upamAnAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.137"
SUTRA_TEXT = "उपमानाच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — upamAnAcca"


class Sutra54137:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.137: अग्निः'),
		('रामः', '', 'प.5.4.137: रामः'),
		('सीता', '', 'प.5.4.137: सीता'),
	]

