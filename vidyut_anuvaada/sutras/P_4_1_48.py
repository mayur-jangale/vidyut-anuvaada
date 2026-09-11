# Sutra प.4.1.48: पुंयोगादाख्यायाम्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.48"
SUTRA_TEXT = "पुंयोगादाख्यायाम्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4148:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

