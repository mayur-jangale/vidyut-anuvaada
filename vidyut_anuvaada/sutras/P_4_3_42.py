# Sutra प.4.3.42: कोशाड्ढञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — koSAqQaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.42"
SUTRA_TEXT = "कोशाड्ढञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — koSAqQaY"


class Sutra4342:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.42: अग्निः'),
		('रामः', '', 'प.4.3.42: रामः'),
		('सीता', '', 'प.4.3.42: सीता'),
	]

