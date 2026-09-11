# Sutra प.4.1.4: अजाद्यतष्टाप्
# vibhakti-sthāna — assign case ending

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.4"
SUTRA_TEXT = "अजाद्यतष्टाप्"
SUTRA_DESC = "vibhakti-sthāna — assign case ending"


class Sutra414:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

