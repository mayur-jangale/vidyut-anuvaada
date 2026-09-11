# Sutra प.8.2.10: झयः
# aparaḥ paraṃ — each earlier rule applies to later

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.10"
SUTRA_TEXT = "झयः"
SUTRA_DESC = "aparaḥ paraṃ — each earlier rule applies to later"


class Sutra8210:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.10: अग्निः'),
		('रामः', '', 'प.8.2.10: रामः'),
		('सीता', '', 'प.8.2.10: सीता'),
	]

