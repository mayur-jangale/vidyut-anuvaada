# Sutra प.6.1.66: लोपो व्योर्वलि
# sandhi-sūtra प.6.1.66

from P_6_1 import apply_6_1_66

SUTRA_CODE = "प.6.1.66"
SUTRA_TEXT = "लोपो व्योर्वलि"
SUTRA_DESC = "sandhi-sūtra प.6.1.66"


class Sutra6166:
	def apply(self, word, pos):
		return apply_6_1_66(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.66:input=अग्निः'),
		('रामः', '', '6.1.66:input=रामः'),
		('सीता', '', '6.1.66:input=सीता'),
	]
