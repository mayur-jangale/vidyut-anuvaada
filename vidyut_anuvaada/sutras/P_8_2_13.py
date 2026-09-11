# Sutra प.8.2.13: उदन्वानुदधौ च
# paratvaṃ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.13"
SUTRA_TEXT = "उदन्वानुदधौ च"
SUTRA_DESC = "paratvaṃ — repeated"


class Sutra8213:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.13: अग्निः'),
		('रामः', '', 'प.8.2.13: रामः'),
		('सीता', '', 'प.8.2.13: सीता'),
	]

