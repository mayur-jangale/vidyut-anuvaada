# Sutra प.4.1.121: द्व्यचः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.121"
SUTRA_TEXT = "द्व्यचः"
SUTRA_DESC = "supaḥ — continued"


class Sutra41121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

