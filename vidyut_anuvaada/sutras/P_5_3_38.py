# Sutra प.5.3.38: उत्तराच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — uttarAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.38"
SUTRA_TEXT = "उत्तराच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — uttarAcca"


class Sutra5338:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.38: अग्निः'),
		('रामः', '', 'प.5.3.38: रामः'),
		('सीता', '', 'प.5.3.38: सीता'),
	]

