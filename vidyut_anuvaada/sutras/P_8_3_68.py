# Sutra प.8.3.68: अवाच्चालम्बनाविदूर्ययोः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.68"
SUTRA_TEXT = "अवाच्चालम्बनाविदूर्ययोः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8368:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.68: अग्निः'),
		('रामः', '', 'प.8.3.68: रामः'),
		('सीता', '', 'प.8.3.68: सीता'),
	]

