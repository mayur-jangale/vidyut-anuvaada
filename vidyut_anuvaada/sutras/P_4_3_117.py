# Sutra प.4.3.117: संज्ञायाम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.117"
SUTRA_TEXT = "संज्ञायाम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAm"


class Sutra43117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.117: अग्निः'),
		('रामः', '', 'प.4.3.117: रामः'),
		('सीता', '', 'प.4.3.117: सीता'),
	]

