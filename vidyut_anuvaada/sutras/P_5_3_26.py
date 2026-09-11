# Sutra प.5.3.26: था हेतौ च च्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — TA hetO ca cCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.26"
SUTRA_TEXT = "था हेतौ च च्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — TA hetO ca cCandasi"


class Sutra5326:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.26: अग्निः'),
		('रामः', '', 'प.5.3.26: रामः'),
		('सीता', '', 'प.5.3.26: सीता'),
	]

