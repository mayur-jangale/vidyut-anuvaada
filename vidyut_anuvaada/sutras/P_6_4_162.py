# Sutra प.6.4.162: विभाषर्जोश्छन्दसि
# (Sandhi (euphonic combination)) — viBAzarjoSCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.162"
SUTRA_TEXT = "विभाषर्जोश्छन्दसि"
SUTRA_DESC = "(Sandhi (euphonic combination)) — viBAzarjoSCandasi"


class Sutra64162:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.162: अग्निः'),
		('रामः', '', 'प.6.4.162: रामः'),
		('सीता', '', 'प.6.4.162: सीता'),
	]

