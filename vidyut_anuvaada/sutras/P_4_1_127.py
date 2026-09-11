# Sutra प.4.1.127: कुलटाया वा
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.127"
SUTRA_TEXT = "कुलटाया वा"
SUTRA_DESC = "supaḥ — continued"


class Sutra41127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

