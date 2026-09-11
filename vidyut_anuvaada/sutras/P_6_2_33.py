# Sutra प.6.2.33: परिप्रत्युपापा वर्ज्यमानाहोरात्रावयवेषु
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.33"
SUTRA_TEXT = "परिप्रत्युपापा वर्ज्यमानाहोरात्रावयवेषु"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6233:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.33: अग्निः'),
		('रामः', '', 'प.6.2.33: रामः'),
		('सीता', '', 'प.6.2.33: सीता'),
	]

