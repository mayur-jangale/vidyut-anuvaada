# Sutra प.6.2.18: पत्यावैश्वर्ये
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.18"
SUTRA_TEXT = "पत्यावैश्वर्ये"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6218:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.18: अग्निः'),
		('रामः', '', 'प.6.2.18: रामः'),
		('सीता', '', 'प.6.2.18: सीता'),
	]

