# Sutra प.4.1.109: लुक् स्त्रियाम्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.109"
SUTRA_TEXT = "लुक् स्त्रियाम्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

