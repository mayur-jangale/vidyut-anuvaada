# Sutra प.4.2.87: कुमुदनडवेतसेभ्यो ड्मतुप्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kumudanaqavetaseByo qmatup

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.87"
SUTRA_TEXT = "कुमुदनडवेतसेभ्यो ड्मतुप्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kumudanaqavetaseByo qmatup"


class Sutra4287:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.87: अग्निः'),
		('रामः', '', 'प.4.2.87: रामः'),
		('सीता', '', 'प.4.2.87: सीता'),
	]

