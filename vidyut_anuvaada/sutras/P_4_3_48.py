# Sutra प.4.3.48: कलाप्यश्वत्थयवबुसाद्वुन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kalApyaSvatTayavabusAdvun

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.48"
SUTRA_TEXT = "कलाप्यश्वत्थयवबुसाद्वुन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kalApyaSvatTayavabusAdvun"


class Sutra4348:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.48: अग्निः'),
		('रामः', '', 'प.4.3.48: रामः'),
		('सीता', '', 'प.4.3.48: सीता'),
	]

