# Sutra प.6.2.10: अध्वर्युकषाययोर्जातौ
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.10"
SUTRA_TEXT = "अध्वर्युकषाययोर्जातौ"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6210:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.10: अग्निः'),
		('रामः', '', 'प.6.2.10: रामः'),
		('सीता', '', 'प.6.2.10: सीता'),
	]

