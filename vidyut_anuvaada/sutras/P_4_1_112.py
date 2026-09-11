# Sutra प.4.1.112: शिवादिभ्योऽण्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.112"
SUTRA_TEXT = "शिवादिभ्योऽण्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

