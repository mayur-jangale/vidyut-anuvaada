# Sutra प.7.3.2: केकयमित्त्रयुप्रलयानां यादेरियः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.2"
SUTRA_TEXT = "केकयमित्त्रयुप्रलयानां यादेरियः"
SUTRA_DESC = "taddhita — continued"


class Sutra732:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.2: अग्निः'),
		('रामः', '', 'प.7.3.2: रामः'),
		('सीता', '', 'प.7.3.2: सीता'),
	]

