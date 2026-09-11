# Sutra प.6.3.131: मन्त्रे सोमाश्वेन्द्रियविश्वदेव्यस्य मतौ
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.131"
SUTRA_TEXT = "मन्त्रे सोमाश्वेन्द्रियविश्वदेव्यस्य मतौ"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.131: अग्निः'),
		('रामः', '', 'प.6.3.131: रामः'),
		('सीता', '', 'प.6.3.131: सीता'),
	]

