# Sutra प.8.3.49: छन्दसि वाऽप्राम्रेडितयोः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.49"
SUTRA_TEXT = "छन्दसि वाऽप्राम्रेडितयोः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8349:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.49: अग्निः'),
		('रामः', '', 'प.8.3.49: रामः'),
		('सीता', '', 'प.8.3.49: सीता'),
	]

