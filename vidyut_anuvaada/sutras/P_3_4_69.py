# Sutra प.3.4.69: लः कर्मणि च भावे चाकर्मकेभ्यः
# yat, kyap — verbal noun suffixes (gamya, gāmaka)

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.69"
SUTRA_TEXT = "लः कर्मणि च भावे चाकर्मकेभ्यः"
SUTRA_DESC = "yat, kyap — verbal noun suffixes (gamya, gāmaka)"


class Sutra3469:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

