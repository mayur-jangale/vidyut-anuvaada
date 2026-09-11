# Sutra प.6.2.56: प्रथमोऽचिरोपसम्पत्तौ
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.56"
SUTRA_TEXT = "प्रथमोऽचिरोपसम्पत्तौ"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6256:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.56: अग्निः'),
		('रामः', '', 'प.6.2.56: रामः'),
		('सीता', '', 'प.6.2.56: सीता'),
	]

