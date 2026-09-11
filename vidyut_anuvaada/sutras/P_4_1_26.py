# Sutra प.4.1.26: संख्याव्ययादेर्ङीप्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.26"
SUTRA_TEXT = "संख्याव्ययादेर्ङीप्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4126:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

