# Sutra प.4.2.6: द्वन्द्वाच्छः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dvandvAcCaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.6"
SUTRA_TEXT = "द्वन्द्वाच्छः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dvandvAcCaH"


class Sutra426:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.6: अग्निः'),
		('रामः', '', 'प.4.2.6: रामः'),
		('सीता', '', 'प.4.2.6: सीता'),
	]

