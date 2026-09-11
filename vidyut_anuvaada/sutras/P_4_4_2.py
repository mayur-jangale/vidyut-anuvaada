# Sutra प.4.4.2: तेन दीव्यति खनति जयति जितम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tena dIvyati Kanati jayati jitam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.2"
SUTRA_TEXT = "तेन दीव्यति खनति जयति जितम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tena dIvyati Kanati jayati jitam"


class Sutra442:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.2: अग्निः'),
		('रामः', '', 'प.4.4.2: रामः'),
		('सीता', '', 'प.4.4.2: सीता'),
	]

