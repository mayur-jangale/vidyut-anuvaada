# Sutra प.7.4.25: अकृत्सार्वधातुकयोर्दीर्घः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.25"
SUTRA_TEXT = "अकृत्सार्वधातुकयोर्दीर्घः"
SUTRA_DESC = "taddhita — continued"


class Sutra7425:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.25: अग्निः'),
		('रामः', '', 'प.7.4.25: रामः'),
		('सीता', '', 'प.7.4.25: सीता'),
	]

