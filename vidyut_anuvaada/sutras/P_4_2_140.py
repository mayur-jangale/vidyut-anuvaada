# Sutra प.4.2.140: राज्ञः क च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — rAjYaH ka ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.140"
SUTRA_TEXT = "राज्ञः क च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — rAjYaH ka ca"


class Sutra42140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.140: अग्निः'),
		('रामः', '', 'प.4.2.140: रामः'),
		('सीता', '', 'प.4.2.140: सीता'),
	]

