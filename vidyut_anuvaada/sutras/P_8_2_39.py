# Sutra प.8.2.39: झलां जशोऽन्ते
# samāptiḥ — end of section

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.39"
SUTRA_TEXT = "झलां जशोऽन्ते"
SUTRA_DESC = "samāptiḥ — end of section"


class Sutra8239:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.39: अग्निः'),
		('रामः', '', 'प.8.2.39: रामः'),
		('सीता', '', 'प.8.2.39: सीता'),
	]

