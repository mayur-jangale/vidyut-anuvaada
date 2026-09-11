# Sutra प.4.1.75: आवट्याच्च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.75"
SUTRA_TEXT = "आवट्याच्च"
SUTRA_DESC = "supaḥ — continued"


class Sutra4175:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

