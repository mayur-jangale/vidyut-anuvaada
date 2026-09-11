# Sutra प.4.3.29: पथः पन्थ च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — paTaH panTa ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.29"
SUTRA_TEXT = "पथः पन्थ च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — paTaH panTa ca"


class Sutra4329:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.29: अग्निः'),
		('रामः', '', 'प.4.3.29: रामः'),
		('सीता', '', 'प.4.3.29: सीता'),
	]

