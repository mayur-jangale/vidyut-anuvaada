# Sutra प.6.2.153: ऊनार्थकलहं तृतीयायाः
# (Sandhi (euphonic combination)) — UnArTakalahaM tftIyAyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.153"
SUTRA_TEXT = "ऊनार्थकलहं तृतीयायाः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — UnArTakalahaM tftIyAyAH"


class Sutra62153:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.153: अग्निः'),
		('रामः', '', 'प.6.2.153: रामः'),
		('सीता', '', 'प.6.2.153: सीता'),
	]

