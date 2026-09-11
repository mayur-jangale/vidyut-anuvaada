# Sutra प.1.2.42: तत्पुरुषः समानाधिकरणः कर्मधारयः
# (Samjna (technical definitions)) — tatpuruzaH samAnADikaraRaH karmaDArayaH

from P_1_2 import apply_1_2_42

SUTRA_CODE = "प.1.2.42"
SUTRA_TEXT = "तत्पुरुषः समानाधिकरणः कर्मधारयः"
SUTRA_DESC = "(Samjna (technical definitions)) — tatpuruzaH samAnADikaraRaH karmaDArayaH"


class Sutra1242:
	def apply(self, word, pos):
		return apply_1_2_42(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'plain-tatpuruṣa:अग्निः'),
		('रामः', '', 'plain-tatpuruṣa:रामः'),
		('सीता', '', 'plain-tatpuruṣa:सीता'),
	]

