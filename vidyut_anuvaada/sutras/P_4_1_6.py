# Sutra प.4.1.6: उगितश्च
# supaḥ — specific sup rules

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.6"
SUTRA_TEXT = "उगितश्च"
SUTRA_DESC = "supaḥ — specific sup rules"


class Sutra416:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

