# Sutra प.8.3.114: प्रतिस्तब्धनिस्तब्धौ च
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.114"
SUTRA_TEXT = "प्रतिस्तब्धनिस्तब्धौ च"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.114: अग्निः'),
		('रामः', '', 'प.8.3.114: रामः'),
		('सीता', '', 'प.8.3.114: सीता'),
	]

