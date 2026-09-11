# Sutra प.6.2.89: अमहन्नवं नगरेऽनुदीचाम्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.89"
SUTRA_TEXT = "अमहन्नवं नगरेऽनुदीचाम्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6289:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.89: अग्निः'),
		('रामः', '', 'प.6.2.89: रामः'),
		('सीता', '', 'प.6.2.89: सीता'),
	]

