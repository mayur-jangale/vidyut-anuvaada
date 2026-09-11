# Sutra प.5.2.125: आलजाटचौ बहुभाषिणि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — AlajAwacO bahuBAziRi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.125"
SUTRA_TEXT = "आलजाटचौ बहुभाषिणि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — AlajAwacO bahuBAziRi"


class Sutra52125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.125: अग्निः'),
		('रामः', '', 'प.5.2.125: रामः'),
		('सीता', '', 'प.5.2.125: सीता'),
	]

