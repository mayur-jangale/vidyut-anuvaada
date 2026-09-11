# Sutra प.4.2.58: घञः साऽस्यां क्रियेति ञः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — GaYaH sA'syAM kriyeti YaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.58"
SUTRA_TEXT = "घञः साऽस्यां क्रियेति ञः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — GaYaH sA'syAM kriyeti YaH"


class Sutra4258:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.58: अग्निः'),
		('रामः', '', 'प.4.2.58: रामः'),
		('सीता', '', 'प.4.2.58: सीता'),
	]

