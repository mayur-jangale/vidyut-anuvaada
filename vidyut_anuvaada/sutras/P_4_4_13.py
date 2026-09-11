# Sutra प.4.4.13: वस्नक्रयविक्रयाट्ठन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vasnakrayavikrayAwWan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.13"
SUTRA_TEXT = "वस्नक्रयविक्रयाट्ठन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vasnakrayavikrayAwWan"


class Sutra4413:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.13: अग्निः'),
		('रामः', '', 'प.4.4.13: रामः'),
		('सीता', '', 'प.4.4.13: सीता'),
	]

