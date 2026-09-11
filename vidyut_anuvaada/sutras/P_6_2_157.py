# Sutra प.6.2.157: अच्कावशक्तौ
# (Sandhi (euphonic combination)) — ackAvaSaktO

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.157"
SUTRA_TEXT = "अच्कावशक्तौ"
SUTRA_DESC = "(Sandhi (euphonic combination)) — ackAvaSaktO"


class Sutra62157:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.157: अग्निः'),
		('रामः', '', 'प.6.2.157: रामः'),
		('सीता', '', 'प.6.2.157: सीता'),
	]

