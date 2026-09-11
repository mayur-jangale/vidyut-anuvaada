# Sutra प.4.1.39: वर्णादनुदात्तात्तोपधात्तो नः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.39"
SUTRA_TEXT = "वर्णादनुदात्तात्तोपधात्तो नः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

