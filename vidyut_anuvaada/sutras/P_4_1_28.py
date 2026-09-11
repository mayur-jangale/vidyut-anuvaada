# Sutra प.4.1.28: अन उपधालोपिनोन्यतरस्याम्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.28"
SUTRA_TEXT = "अन उपधालोपिनोन्यतरस्याम्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

