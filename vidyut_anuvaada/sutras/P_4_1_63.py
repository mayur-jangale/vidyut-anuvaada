# Sutra प.4.1.63: जातेरस्त्रीविषयादयोपधात्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.63"
SUTRA_TEXT = "जातेरस्त्रीविषयादयोपधात्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4163:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

