# Sutra प.4.1.54: स्वाङ्गाच्चोपसर्जनादसंयोगोपधात्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.54"
SUTRA_TEXT = "स्वाङ्गाच्चोपसर्जनादसंयोगोपधात्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4154:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

