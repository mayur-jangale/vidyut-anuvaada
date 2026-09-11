# Sutra प.6.3.115: कर्णे लक्षणस्याविष्टाष्टपञ्चमणिभिन्नछिन्नछिद्रस्रुवस्वस्तिकस्य
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.115"
SUTRA_TEXT = "कर्णे लक्षणस्याविष्टाष्टपञ्चमणिभिन्नछिन्नछिद्रस्रुवस्वस्तिकस्य"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.115: अग्निः'),
		('रामः', '', 'प.6.3.115: रामः'),
		('सीता', '', 'प.6.3.115: सीता'),
	]

