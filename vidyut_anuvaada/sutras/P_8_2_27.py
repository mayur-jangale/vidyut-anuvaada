# Sutra प.8.2.27: ह्रस्वादङ्गात्
# pūrvatrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.27"
SUTRA_TEXT = "ह्रस्वादङ्गात्"
SUTRA_DESC = "pūrvatrāsiddham — repeated"


class Sutra8227:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.27: अग्निः'),
		('रामः', '', 'प.8.2.27: रामः'),
		('सीता', '', 'प.8.2.27: सीता'),
	]

