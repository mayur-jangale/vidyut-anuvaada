# Sutra प.4.2.88: नडशादाड्ड्वलच्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — naqaSAdAqqvalac

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.88"
SUTRA_TEXT = "नडशादाड्ड्वलच्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — naqaSAdAqqvalac"


class Sutra4288:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.88: अग्निः'),
		('रामः', '', 'प.4.2.88: रामः'),
		('सीता', '', 'प.4.2.88: सीता'),
	]

