# Sutra प.6.4.58: युप्लुवोर्दीर्घश्छन्दसि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.58"
SUTRA_TEXT = "युप्लुवोर्दीर्घश्छन्दसि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6458:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.58: अग्निः'),
		('रामः', '', 'प.6.4.58: रामः'),
		('सीता', '', 'प.6.4.58: सीता'),
	]

