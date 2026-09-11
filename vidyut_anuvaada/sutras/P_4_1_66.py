# Sutra प.4.1.66: ऊङुतः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.66"
SUTRA_TEXT = "ऊङुतः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4166:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

