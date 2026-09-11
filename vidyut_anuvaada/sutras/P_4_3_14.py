# Sutra प.4.3.14: निशाप्रदोषाभ्यां च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — niSApradozAByAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.14"
SUTRA_TEXT = "निशाप्रदोषाभ्यां च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — niSApradozAByAM ca"


class Sutra4314:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.14: अग्निः'),
		('रामः', '', 'प.4.3.14: रामः'),
		('सीता', '', 'प.4.3.14: सीता'),
	]

