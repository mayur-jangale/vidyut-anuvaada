# Sutra प.4.1.57: सहनञ्विद्यमानपूर्वाच्च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.57"
SUTRA_TEXT = "सहनञ्विद्यमानपूर्वाच्च"
SUTRA_DESC = "supaḥ — continued"


class Sutra4157:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

