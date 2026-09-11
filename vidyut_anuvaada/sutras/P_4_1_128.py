# Sutra प.4.1.128: चटकाया ऐरक्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.128"
SUTRA_TEXT = "चटकाया ऐरक्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

