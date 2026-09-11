# Sutra प.6.2.21: आशङ्काबाधनेदीयस्सु संभावने
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.21"
SUTRA_TEXT = "आशङ्काबाधनेदीयस्सु संभावने"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6221:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.21: अग्निः'),
		('रामः', '', 'प.6.2.21: रामः'),
		('सीता', '', 'प.6.2.21: सीता'),
	]

