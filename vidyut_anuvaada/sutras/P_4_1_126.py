# Sutra प.4.1.126: कल्याण्यादीनामिनङ्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.126"
SUTRA_TEXT = "कल्याण्यादीनामिनङ्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41126:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

