# Sutra प.6.2.105: उत्तरपदवृद्धौ सर्वं च
# (Sandhi (euphonic combination)) — uttarapadavfdDO sarvaM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.105"
SUTRA_TEXT = "उत्तरपदवृद्धौ सर्वं च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — uttarapadavfdDO sarvaM ca"


class Sutra62105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.105: अग्निः'),
		('रामः', '', 'प.6.2.105: रामः'),
		('सीता', '', 'प.6.2.105: सीता'),
	]

