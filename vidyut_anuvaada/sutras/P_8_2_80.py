# Sutra प.8.2.80: अदसोऽसेर्दादु दो मः
# (Final transformations (tripāḍī)) — adaso'serdAdu do maH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.80"
SUTRA_TEXT = "अदसोऽसेर्दादु दो मः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — adaso'serdAdu do maH"


class Sutra8280:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.80: अग्निः'),
		('रामः', '', 'प.8.2.80: रामः'),
		('सीता', '', 'प.8.2.80: सीता'),
	]

