# Sutra प.4.4.104: पथ्यतिथिवसतिस्वपतेर्ढञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — paTyatiTivasatisvapaterQaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.104"
SUTRA_TEXT = "पथ्यतिथिवसतिस्वपतेर्ढञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — paTyatiTivasatisvapaterQaY"


class Sutra44104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.104: अग्निः'),
		('रामः', '', 'प.4.4.104: रामः'),
		('सीता', '', 'प.4.4.104: सीता'),
	]

