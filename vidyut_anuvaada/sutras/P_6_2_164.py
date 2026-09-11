# Sutra प.6.2.164: विभाषा छन्दसि
# (Sandhi (euphonic combination)) — viBAzA Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.164"
SUTRA_TEXT = "विभाषा छन्दसि"
SUTRA_DESC = "(Sandhi (euphonic combination)) — viBAzA Candasi"


class Sutra62164:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.164: अग्निः'),
		('रामः', '', 'प.6.2.164: रामः'),
		('सीता', '', 'प.6.2.164: सीता'),
	]

