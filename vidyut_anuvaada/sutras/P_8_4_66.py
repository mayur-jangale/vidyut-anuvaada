# Sutra प.8.4.66: उदात्तादनुदात्तस्य स्वरितः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.66"
SUTRA_TEXT = "उदात्तादनुदात्तस्य स्वरितः"
SUTRA_DESC = "final transformations — continued"


class Sutra8466:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.66: अग्निः'),
		('रामः', '', 'प.8.4.66: रामः'),
		('सीता', '', 'प.8.4.66: सीता'),
	]

