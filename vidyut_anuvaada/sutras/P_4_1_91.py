# Sutra प.4.1.91: फक्फिञोरन्यतरस्याम्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.91"
SUTRA_TEXT = "फक्फिञोरन्यतरस्याम्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4191:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

