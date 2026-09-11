# Sutra प.3.1.17: शब्दवैरकलहाभ्रकण्वमेघेभ्यः करणे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — SabdavErakalahABrakaRvameGeByaH karaRe

from P_3_1 import apply_3_1_17

SUTRA_CODE = "प.3.1.17"
SUTRA_TEXT = "शब्दवैरकलहाभ्रकण्वमेघेभ्यः करणे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — SabdavErakalahABrakaRvameGeByaH karaRe"


class Sutra3117:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_17(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.17:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.17:root=रामः;pos='),
		('सीता', '', 'प.3.1.17:root=सीता;pos='),
	]

