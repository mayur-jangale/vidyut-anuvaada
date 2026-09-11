# Sutra प.4.3.27: संज्ञायां शरदो वुञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAM Sarado vuY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.27"
SUTRA_TEXT = "संज्ञायां शरदो वुञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAM Sarado vuY"


class Sutra4327:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.27: अग्निः'),
		('रामः', '', 'प.4.3.27: रामः'),
		('सीता', '', 'प.4.3.27: सीता'),
	]

