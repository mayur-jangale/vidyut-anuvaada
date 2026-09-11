# Sutra प.4.2.145: कृकणपर्णाद्भारद्वाजे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kfkaRaparRAdBAradvAje

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.145"
SUTRA_TEXT = "कृकणपर्णाद्भारद्वाजे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kfkaRaparRAdBAradvAje"


class Sutra42145:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.145: अग्निः'),
		('रामः', '', 'प.4.2.145: रामः'),
		('सीता', '', 'प.4.2.145: सीता'),
	]

