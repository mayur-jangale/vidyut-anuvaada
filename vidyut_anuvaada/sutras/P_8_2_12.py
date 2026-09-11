# Sutra प.8.2.12: आसन्दीवदष्ठीवच्चक्रीवत्कक्षीवद्रुमण्वच्चर्मण्वती
# uttaratrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.12"
SUTRA_TEXT = "आसन्दीवदष्ठीवच्चक्रीवत्कक्षीवद्रुमण्वच्चर्मण्वती"
SUTRA_DESC = "uttaratrāsiddham — repeated"


class Sutra8212:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.12: अग्निः'),
		('रामः', '', 'प.8.2.12: रामः'),
		('सीता', '', 'प.8.2.12: सीता'),
	]

