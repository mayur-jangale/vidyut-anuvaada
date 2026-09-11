# Sutra प.8.3.92: प्रष्ठोऽग्रगामिनि
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.92"
SUTRA_TEXT = "प्रष्ठोऽग्रगामिनि"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8392:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.92: अग्निः'),
		('रामः', '', 'प.8.3.92: रामः'),
		('सीता', '', 'प.8.3.92: सीता'),
	]

