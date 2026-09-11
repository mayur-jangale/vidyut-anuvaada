# Sutra प.5.3.79: घनिलचौ च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — GanilacO ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.79"
SUTRA_TEXT = "घनिलचौ च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — GanilacO ca"


class Sutra5379:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.79: अग्निः'),
		('रामः', '', 'प.5.3.79: रामः'),
		('सीता', '', 'प.5.3.79: सीता'),
	]

