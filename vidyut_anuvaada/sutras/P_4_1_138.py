# Sutra प.4.1.138: क्षत्राद्घः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.138"
SUTRA_TEXT = "क्षत्राद्घः"
SUTRA_DESC = "supaḥ — continued"


class Sutra41138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

