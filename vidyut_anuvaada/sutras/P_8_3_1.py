# Sutra प.8.3.1: मतुवसो रु सम्बुद्धौ छन्दसि
# pūrvatrāsiddhamuttaratrāsiddhaṃ tripāḍī bhavataḥ — tripāḍī rules have special ordering

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.1"
SUTRA_TEXT = "मतुवसो रु सम्बुद्धौ छन्दसि"
SUTRA_DESC = "pūrvatrāsiddhamuttaratrāsiddhaṃ tripāḍī bhavataḥ — tripāḍī rules have special ordering"


class Sutra831:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.1: अग्निः'),
		('रामः', '', 'प.8.3.1: रामः'),
		('सीता', '', 'प.8.3.1: सीता'),
	]

