# Sutra प.4.2.47: अचित्तहस्तिधेनोष्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — acittahastiDenozWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.47"
SUTRA_TEXT = "अचित्तहस्तिधेनोष्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — acittahastiDenozWak"


class Sutra4247:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.47: अग्निः'),
		('रामः', '', 'प.4.2.47: रामः'),
		('सीता', '', 'प.4.2.47: सीता'),
	]

