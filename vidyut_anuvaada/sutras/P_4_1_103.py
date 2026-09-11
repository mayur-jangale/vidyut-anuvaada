# Sutra प.4.1.103: द्रोणपर्वतजीवन्तादन्यतरस्याम्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.103"
SUTRA_TEXT = "द्रोणपर्वतजीवन्तादन्यतरस्याम्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

