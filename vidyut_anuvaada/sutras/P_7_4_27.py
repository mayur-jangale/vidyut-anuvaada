# Sutra प.7.4.27: रीङ् ऋतः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.27"
SUTRA_TEXT = "रीङ् ऋतः"
SUTRA_DESC = "taddhita — continued"


class Sutra7427:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.27: अग्निः'),
		('रामः', '', 'प.7.4.27: रामः'),
		('सीता', '', 'प.7.4.27: सीता'),
	]

