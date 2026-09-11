# Sutra प.5.3.77: नीतौ च तद्युक्तात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — nItO ca tadyuktAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.77"
SUTRA_TEXT = "नीतौ च तद्युक्तात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — nItO ca tadyuktAt"


class Sutra5377:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.77: अग्निः'),
		('रामः', '', 'प.5.3.77: रामः'),
		('सीता', '', 'प.5.3.77: सीता'),
	]

