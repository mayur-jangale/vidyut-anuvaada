# Sutra प.5.2.95: रसादिभ्यश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — rasAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.95"
SUTRA_TEXT = "रसादिभ्यश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — rasAdiByaSca"


class Sutra5295:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.95: अग्निः'),
		('रामः', '', 'प.5.2.95: रामः'),
		('सीता', '', 'प.5.2.95: सीता'),
	]

