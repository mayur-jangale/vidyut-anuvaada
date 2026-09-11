# Sutra प.8.2.3: न मु ने
# paratvaṃ — priority of later rules

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.3"
SUTRA_TEXT = "न मु ने"
SUTRA_DESC = "paratvaṃ — priority of later rules"


class Sutra823:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.3: अग्निः'),
		('रामः', '', 'प.8.2.3: रामः'),
		('सीता', '', 'प.8.2.3: सीता'),
	]

