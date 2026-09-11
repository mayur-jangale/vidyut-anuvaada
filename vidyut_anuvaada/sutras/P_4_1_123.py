# Sutra प.4.1.123: शुभ्रादिभ्यश्च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.123"
SUTRA_TEXT = "शुभ्रादिभ्यश्च"
SUTRA_DESC = "supaḥ — continued"


class Sutra41123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

