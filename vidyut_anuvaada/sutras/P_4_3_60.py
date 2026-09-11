# Sutra प.4.3.60: अन्तःपूर्वपदाट्ठञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — antaHpUrvapadAwWaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.60"
SUTRA_TEXT = "अन्तःपूर्वपदाट्ठञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — antaHpUrvapadAwWaY"


class Sutra4360:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.60: अग्निः'),
		('रामः', '', 'प.4.3.60: रामः'),
		('सीता', '', 'प.4.3.60: सीता'),
	]

