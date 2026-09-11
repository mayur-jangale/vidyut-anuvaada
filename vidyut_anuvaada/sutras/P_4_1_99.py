# Sutra प.4.1.99: नडादिभ्यः फक्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.99"
SUTRA_TEXT = "नडादिभ्यः फक्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4199:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

