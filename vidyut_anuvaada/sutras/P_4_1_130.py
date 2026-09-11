# Sutra प.4.1.130: आरगुदीचाम्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.130"
SUTRA_TEXT = "आरगुदीचाम्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

