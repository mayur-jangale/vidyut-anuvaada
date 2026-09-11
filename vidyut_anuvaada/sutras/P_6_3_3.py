# Sutra प.6.3.3: ओजःसहोऽम्भस्तमसः तृतीयायाः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.3"
SUTRA_TEXT = "ओजःसहोऽम्भस्तमसः तृतीयायाः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra633:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.3: अग्निः'),
		('रामः', '', 'प.6.3.3: रामः'),
		('सीता', '', 'प.6.3.3: सीता'),
	]

