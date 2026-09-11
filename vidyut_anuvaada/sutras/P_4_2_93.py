# Sutra प.4.2.93: राष्ट्रावारपाराद्घखौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — rAzwrAvArapArAdGaKO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.93"
SUTRA_TEXT = "राष्ट्रावारपाराद्घखौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — rAzwrAvArapArAdGaKO"


class Sutra4293:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.93: अग्निः'),
		('रामः', '', 'प.4.2.93: रामः'),
		('सीता', '', 'प.4.2.93: सीता'),
	]

