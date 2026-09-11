# Sutra प.8.4.58: अनुस्वारस्य ययि परसवर्णः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.58"
SUTRA_TEXT = "अनुस्वारस्य ययि परसवर्णः"
SUTRA_DESC = "final transformations — continued"


class Sutra8458:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.58: अग्निः'),
		('रामः', '', 'प.8.4.58: रामः'),
		('सीता', '', 'प.8.4.58: सीता'),
	]

