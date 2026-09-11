# Sutra प.4.3.77: विद्यायोनिसंबन्धेभ्यो वुञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vidyAyonisaMbanDeByo vuY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.77"
SUTRA_TEXT = "विद्यायोनिसंबन्धेभ्यो वुञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vidyAyonisaMbanDeByo vuY"


class Sutra4377:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.77: अग्निः'),
		('रामः', '', 'प.4.3.77: रामः'),
		('सीता', '', 'प.4.3.77: सीता'),
	]

