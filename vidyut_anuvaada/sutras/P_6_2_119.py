# Sutra प.6.2.119: आद्युदात्तं द्व्यच् छन्दसि
# (Sandhi (euphonic combination)) — AdyudAttaM dvyac Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.119"
SUTRA_TEXT = "आद्युदात्तं द्व्यच् छन्दसि"
SUTRA_DESC = "(Sandhi (euphonic combination)) — AdyudAttaM dvyac Candasi"


class Sutra62119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.119: अग्निः'),
		('रामः', '', 'प.6.2.119: रामः'),
		('सीता', '', 'प.6.2.119: सीता'),
	]

