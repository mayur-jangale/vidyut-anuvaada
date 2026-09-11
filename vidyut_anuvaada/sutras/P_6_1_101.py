# Sutra प.6.1.101: अकः सवर्णे दीर्घः
# sandhi-sūtra प.6.1.101

from P_6_1 import apply_6_1_101

SUTRA_CODE = "प.6.1.101"
SUTRA_TEXT = "अकः सवर्णे दीर्घः"
SUTRA_DESC = "sandhi-sūtra प.6.1.101"


class Sutra61101:
	def apply(self, word, pos):
		return apply_6_1_101(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.101:input=अग्निः'),
		('रामः', '', '6.1.101:input=रामः'),
		('सीता', '', '6.1.101:input=सीता'),
	]
