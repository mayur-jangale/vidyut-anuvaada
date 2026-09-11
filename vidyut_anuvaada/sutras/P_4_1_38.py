# Sutra प.4.1.38: मनोरौ वा
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.38"
SUTRA_TEXT = "मनोरौ वा"
SUTRA_DESC = "supaḥ — continued"


class Sutra4138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

