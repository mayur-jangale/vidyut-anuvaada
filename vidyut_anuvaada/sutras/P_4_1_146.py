# Sutra प.4.1.146: रेवत्यादिभ्यष्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — revatyAdiByazWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.146"
SUTRA_TEXT = "रेवत्यादिभ्यष्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — revatyAdiByazWak"


class Sutra41146:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

