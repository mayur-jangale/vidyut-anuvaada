# Sutra प.8.4.3: पूर्वपदात् संज्ञायामगः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.3"
SUTRA_TEXT = "पूर्वपदात् संज्ञायामगः"
SUTRA_DESC = "final transformations — continued"


class Sutra843:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.3: अग्निः'),
		('रामः', '', 'प.8.4.3: रामः'),
		('सीता', '', 'प.8.4.3: सीता'),
	]

