# Sutra प.4.1.137: राजश्वशुराद्यत्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.137"
SUTRA_TEXT = "राजश्वशुराद्यत्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41137:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

