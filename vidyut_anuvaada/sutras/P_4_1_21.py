# Sutra प.4.1.21: द्विगोः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.21"
SUTRA_TEXT = "द्विगोः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

