# Sutra प.6.2.140: उभे वनस्पत्यादिषु युगपत्
# (Sandhi (euphonic combination)) — uBe vanaspatyAdizu yugapat

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.140"
SUTRA_TEXT = "उभे वनस्पत्यादिषु युगपत्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — uBe vanaspatyAdizu yugapat"


class Sutra62140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.140: अग्निः'),
		('रामः', '', 'प.6.2.140: रामः'),
		('सीता', '', 'प.6.2.140: सीता'),
	]

