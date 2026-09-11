# Sutra प.4.1.134: मातृष्वसुश्च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.134"
SUTRA_TEXT = "मातृष्वसुश्च"
SUTRA_DESC = "supaḥ — continued"


class Sutra41134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

