# Sutra प.8.1.8: वाक्यादेरामन्त्रितस्यासूयासम्मतिकोपकुत्सनभर्त्सनेषु
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.8"
SUTRA_TEXT = "वाक्यादेरामन्त्रितस्यासूयासम्मतिकोपकुत्सनभर्त्सनेषु"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra818:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.8: अग्निः'),
		('रामः', '', 'प.8.1.8: रामः'),
		('सीता', '', 'प.8.1.8: सीता'),
	]

