# Sutra प.4.1.50: क्रीतात् करणपूर्वात्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.50"
SUTRA_TEXT = "क्रीतात् करणपूर्वात्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4150:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

