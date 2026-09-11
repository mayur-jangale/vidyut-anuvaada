# Sutra प.1.4.13: यस्मात् प्रत्ययविधिस्तदादि प्रत्ययेऽङ्गम्
# yāsvat — long ā becomes short a before sṛṇvat

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.13"
SUTRA_TEXT = "यस्मात् प्रत्ययविधिस्तदादि प्रत्ययेऽङ्गम्"
SUTRA_DESC = "yāsvat — long ā becomes short a before sṛṇvat"


class Sutra1413:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_13
		return apply_1_4_13(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-anga:अग्निः'),
		('रामः', '', 'not-anga:रामः'),
		('सीता', '', 'not-anga:सीता'),
	]

