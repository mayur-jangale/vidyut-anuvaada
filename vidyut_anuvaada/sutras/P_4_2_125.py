# Sutra प.4.2.125: अवृद्धादपि बहुवचनविषयात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — avfdDAdapi bahuvacanavizayAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.125"
SUTRA_TEXT = "अवृद्धादपि बहुवचनविषयात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — avfdDAdapi bahuvacanavizayAt"


class Sutra42125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.125: अग्निः'),
		('रामः', '', 'प.4.2.125: रामः'),
		('सीता', '', 'प.4.2.125: सीता'),
	]

