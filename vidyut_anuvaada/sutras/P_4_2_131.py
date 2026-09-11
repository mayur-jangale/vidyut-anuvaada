# Sutra प.4.2.131: मद्रवृज्योः कन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — madravfjyoH kan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.131"
SUTRA_TEXT = "मद्रवृज्योः कन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — madravfjyoH kan"


class Sutra42131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.131: अग्निः'),
		('रामः', '', 'प.4.2.131: रामः'),
		('सीता', '', 'प.4.2.131: सीता'),
	]

