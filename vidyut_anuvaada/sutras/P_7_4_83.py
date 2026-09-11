# Sutra प.7.4.83: दीर्घोऽकितः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.83"
SUTRA_TEXT = "दीर्घोऽकितः"
SUTRA_DESC = "taddhita — continued"


class Sutra7483:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.83: अग्निः'),
		('रामः', '', 'प.7.4.83: रामः'),
		('सीता', '', 'प.7.4.83: सीता'),
	]

