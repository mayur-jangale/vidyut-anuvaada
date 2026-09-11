# Sutra प.4.4.20: क्त्रेर्मम् नित्यं
# (Sup-sthāna (nominal endings) and kṛt-affixes) — ktrermam nityaM

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.20"
SUTRA_TEXT = "क्त्रेर्मम् नित्यं"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — ktrermam nityaM"


class Sutra4420:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.20: अग्निः'),
		('रामः', '', 'प.4.4.20: रामः'),
		('सीता', '', 'प.4.4.20: सीता'),
	]

