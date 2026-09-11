# Sutra प.4.1.118: पीलाया वा
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.118"
SUTRA_TEXT = "पीलाया वा"
SUTRA_DESC = "supaḥ — continued"


class Sutra41118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

