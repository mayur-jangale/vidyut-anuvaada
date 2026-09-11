# Sutra प.4.1.79: गोत्रावयवात्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.79"
SUTRA_TEXT = "गोत्रावयवात्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4179:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

