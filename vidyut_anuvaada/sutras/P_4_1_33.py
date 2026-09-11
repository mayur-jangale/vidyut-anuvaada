# Sutra प.4.1.33: पत्युर्नो यज्ञसंयोगे
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.33"
SUTRA_TEXT = "पत्युर्नो यज्ञसंयोगे"
SUTRA_DESC = "supaḥ — continued"


class Sutra4133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

