# Sutra प.7.4.84: नीग्वञ्चुस्रंसुध्वंसुभ्रंसुकसपतपदस्कन्दाम्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.84"
SUTRA_TEXT = "नीग्वञ्चुस्रंसुध्वंसुभ्रंसुकसपतपदस्कन्दाम्"
SUTRA_DESC = "taddhita — continued"


class Sutra7484:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.84: अग्निः'),
		('रामः', '', 'प.7.4.84: रामः'),
		('सीता', '', 'प.7.4.84: सीता'),
	]

