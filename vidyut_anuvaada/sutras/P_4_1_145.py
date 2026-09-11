# Sutra प.4.1.145: व्यन् सपत्ने
# supaḥ — final rule of sup-sthāna

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.145"
SUTRA_TEXT = "व्यन् सपत्ने"
SUTRA_DESC = "supaḥ — final rule of sup-sthāna"


class Sutra41145:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

