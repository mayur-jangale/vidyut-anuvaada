# Sutra प.4.2.102: कन्थायाष्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kanTAyAzWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.102"
SUTRA_TEXT = "कन्थायाष्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kanTAyAzWak"


class Sutra42102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.102: अग्निः'),
		('रामः', '', 'प.4.2.102: रामः'),
		('सीता', '', 'प.4.2.102: सीता'),
	]

