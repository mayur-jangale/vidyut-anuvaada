# Sutra प.4.1.111: भर्गात् त्रैगर्ते
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.111"
SUTRA_TEXT = "भर्गात् त्रैगर्ते"
SUTRA_DESC = "supaḥ — continued"


class Sutra41111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

