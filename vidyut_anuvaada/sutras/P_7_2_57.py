# Sutra प.7.2.57: सेऽसिचि कृतचृतच्छृदतृदनृतः
# (Taddhita (secondary derivations)) — se'sici kftacftacCfdatfdanftaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.57"
SUTRA_TEXT = "सेऽसिचि कृतचृतच्छृदतृदनृतः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — se'sici kftacftacCfdatfdanftaH"


class Sutra7257:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.57: अग्निः'),
		('रामः', '', 'प.7.2.57: रामः'),
		('सीता', '', 'प.7.2.57: सीता'),
	]

