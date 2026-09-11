# Sutra प.4.1.76: तद्धिताः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.76"
SUTRA_TEXT = "तद्धिताः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4176:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

