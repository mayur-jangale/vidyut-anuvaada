# Sutra प.4.4.10: पर्पादिभ्यः ष्ठन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — parpAdiByaH zWan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.10"
SUTRA_TEXT = "पर्पादिभ्यः ष्ठन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — parpAdiByaH zWan"


class Sutra4410:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.10: अग्निः'),
		('रामः', '', 'प.4.4.10: रामः'),
		('सीता', '', 'प.4.4.10: सीता'),
	]

