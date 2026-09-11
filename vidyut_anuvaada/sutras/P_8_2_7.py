# Sutra प.8.2.7: नलोपः प्रातिपदिकान्तस्य
# padasya ca halantasya — word-final consonants are treated specially

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.7"
SUTRA_TEXT = "नलोपः प्रातिपदिकान्तस्य"
SUTRA_DESC = "padasya ca halantasya — word-final consonants are treated specially"


class Sutra827:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.7: अग्निः'),
		('रामः', '', 'प.8.2.7: रामः'),
		('सीता', '', 'प.8.2.7: सीता'),
	]

