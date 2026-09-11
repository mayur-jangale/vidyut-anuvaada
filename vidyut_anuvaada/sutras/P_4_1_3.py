# Sutra प.4.1.3: स्त्रियाम्
# liṅga-sthāna — assign gender (puṃ/stri/napuṃsaka)

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.3"
SUTRA_TEXT = "स्त्रियाम्"
SUTRA_DESC = "liṅga-sthāna — assign gender (puṃ/stri/napuṃsaka)"


class Sutra413:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

