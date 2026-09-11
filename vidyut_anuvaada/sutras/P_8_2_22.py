# Sutra प.8.2.22: परेश्च घाङ्कयोः
# aparatvaṃ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.22"
SUTRA_TEXT = "परेश्च घाङ्कयोः"
SUTRA_DESC = "aparatvaṃ — repeated"


class Sutra8222:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.22: अग्निः'),
		('रामः', '', 'प.8.2.22: रामः'),
		('सीता', '', 'प.8.2.22: सीता'),
	]

