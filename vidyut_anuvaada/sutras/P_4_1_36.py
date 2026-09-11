# Sutra प.4.1.36: पूतक्रतोरै च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.36"
SUTRA_TEXT = "पूतक्रतोरै च"
SUTRA_DESC = "supaḥ — continued"


class Sutra4136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

