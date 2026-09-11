# Sutra प.4.1.92: तस्यापत्यम्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.92"
SUTRA_TEXT = "तस्यापत्यम्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4192:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

