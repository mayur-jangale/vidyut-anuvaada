# Sutra प.4.1.115: मातुरुत् संख्यासम्भद्रपूर्वायाः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.115"
SUTRA_TEXT = "मातुरुत् संख्यासम्भद्रपूर्वायाः"
SUTRA_DESC = "supaḥ — continued"


class Sutra41115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

