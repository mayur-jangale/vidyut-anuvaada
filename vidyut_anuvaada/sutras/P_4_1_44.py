# Sutra प.4.1.44: वोतो गुणवचनात्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.44"
SUTRA_TEXT = "वोतो गुणवचनात्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4144:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

