# Sutra प.8.4.68: अ अ
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.68"
SUTRA_TEXT = "अ अ"
SUTRA_DESC = "final transformations — continued"


class Sutra8468:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.68: अग्निः'),
		('रामः', '', 'प.8.4.68: रामः'),
		('सीता', '', 'प.8.4.68: सीता'),
	]

