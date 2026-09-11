# Sutra प.4.3.6: दिक्पूर्वपदाट्ठञ् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dikpUrvapadAwWaY ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.6"
SUTRA_TEXT = "दिक्पूर्वपदाट्ठञ् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dikpUrvapadAwWaY ca"


class Sutra436:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.6: अग्निः'),
		('रामः', '', 'प.4.3.6: रामः'),
		('सीता', '', 'प.4.3.6: सीता'),
	]

