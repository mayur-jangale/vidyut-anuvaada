# Sutra प.6.2.25: श्रज्याऽवमकन्पापवत्सु भावे कर्मधारये
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.25"
SUTRA_TEXT = "श्रज्याऽवमकन्पापवत्सु भावे कर्मधारये"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6225:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.25: अग्निः'),
		('रामः', '', 'प.6.2.25: रामः'),
		('सीता', '', 'प.6.2.25: सीता'),
	]

