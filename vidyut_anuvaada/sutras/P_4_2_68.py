# Sutra प.4.2.68: तेन निर्वृत्तम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tena nirvfttam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.68"
SUTRA_TEXT = "तेन निर्वृत्तम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tena nirvfttam"


class Sutra4268:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.68: अग्निः'),
		('रामः', '', 'प.4.2.68: रामः'),
		('सीता', '', 'प.4.2.68: सीता'),
	]

