# Sutra प.5.2.6: यथामुखसंमुखस्य दर्शनः खः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.6"
SUTRA_TEXT = "यथामुखसंमुखस्य दर्शनः खः"
SUTRA_DESC = "taddhita — continued"


class Sutra526:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.6: अग्निः'),
		('रामः', '', 'प.5.2.6: रामः'),
		('सीता', '', 'प.5.2.6: सीता'),
	]

