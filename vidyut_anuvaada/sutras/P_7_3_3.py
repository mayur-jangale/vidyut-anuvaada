# Sutra प.7.3.3: न य्वाभ्यां पदान्ताभ्याम् पूर्वौ तु ताभ्यामैच्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.3"
SUTRA_TEXT = "न य्वाभ्यां पदान्ताभ्याम् पूर्वौ तु ताभ्यामैच्"
SUTRA_DESC = "taddhita — continued"


class Sutra733:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.3: अग्निः'),
		('रामः', '', 'प.7.3.3: रामः'),
		('सीता', '', 'प.7.3.3: सीता'),
	]

