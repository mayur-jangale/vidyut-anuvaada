# Sutra प.4.3.49: ग्रीष्मावरसमाद्वुञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — grIzmAvarasamAdvuY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.49"
SUTRA_TEXT = "ग्रीष्मावरसमाद्वुञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — grIzmAvarasamAdvuY"


class Sutra4349:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.49: अग्निः'),
		('रामः', '', 'प.4.3.49: रामः'),
		('सीता', '', 'प.4.3.49: सीता'),
	]

