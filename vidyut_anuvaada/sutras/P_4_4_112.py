# Sutra प.4.4.112: वेशन्तहिमवद्भ्यामण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — veSantahimavadByAmaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.112"
SUTRA_TEXT = "वेशन्तहिमवद्भ्यामण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — veSantahimavadByAmaR"


class Sutra44112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.112: अग्निः'),
		('रामः', '', 'प.4.4.112: रामः'),
		('सीता', '', 'प.4.4.112: सीता'),
	]

