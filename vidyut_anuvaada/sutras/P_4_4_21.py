# Sutra प.4.4.21: अपमित्ययाचिताभ्यां कक्कनौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — apamityayAcitAByAM kakkanO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.21"
SUTRA_TEXT = "अपमित्ययाचिताभ्यां कक्कनौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — apamityayAcitAByAM kakkanO"


class Sutra4421:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.21: अग्निः'),
		('रामः', '', 'प.4.4.21: रामः'),
		('सीता', '', 'प.4.4.21: सीता'),
	]

