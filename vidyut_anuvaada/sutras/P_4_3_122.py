# Sutra प.4.3.122: पत्रपूर्वादञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — patrapUrvAdaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.122"
SUTRA_TEXT = "पत्रपूर्वादञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — patrapUrvAdaY"


class Sutra43122:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.122: अग्निः'),
		('रामः', '', 'प.4.3.122: रामः'),
		('सीता', '', 'प.4.3.122: सीता'),
	]

