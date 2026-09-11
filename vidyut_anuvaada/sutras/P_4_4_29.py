# Sutra प.4.4.29: परिमुखं च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — parimuKaM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.29"
SUTRA_TEXT = "परिमुखं च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — parimuKaM ca"


class Sutra4429:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.29: अग्निः'),
		('रामः', '', 'प.4.4.29: रामः'),
		('सीता', '', 'प.4.4.29: सीता'),
	]

