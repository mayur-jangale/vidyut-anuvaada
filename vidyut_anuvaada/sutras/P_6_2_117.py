# Sutra प.6.2.117: सोर्मनसी अलोमोषसी
# (Sandhi (euphonic combination)) — sormanasI alomozasI

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.117"
SUTRA_TEXT = "सोर्मनसी अलोमोषसी"
SUTRA_DESC = "(Sandhi (euphonic combination)) — sormanasI alomozasI"


class Sutra62117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.117: अग्निः'),
		('रामः', '', 'प.6.2.117: रामः'),
		('सीता', '', 'प.6.2.117: सीता'),
	]

