# Sutra प.4.1.125: भ्रुवो वुक् च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.125"
SUTRA_TEXT = "भ्रुवो वुक् च"
SUTRA_DESC = "supaḥ — continued"


class Sutra41125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

