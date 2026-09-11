# Sutra प.4.1.41: षिद्गौरादिभ्यश्च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.41"
SUTRA_TEXT = "षिद्गौरादिभ्यश्च"
SUTRA_DESC = "supaḥ — continued"


class Sutra4141:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

