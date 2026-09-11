# Sutra प.7.4.1: णौ चङ्युपधाया ह्रस्वः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.1"
SUTRA_TEXT = "णौ चङ्युपधाया ह्रस्वः"
SUTRA_DESC = "taddhita — continued"


class Sutra741:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.1: अग्निः'),
		('रामः', '', 'प.7.4.1: रामः'),
		('सीता', '', 'प.7.4.1: सीता'),
	]

