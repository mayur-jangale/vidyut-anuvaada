# Sutra प.6.4.175: ऋत्व्यवास्त्व्यवास्त्वमाध्वीहिरण्ययानि च्छन्दसि
# (Sandhi (euphonic combination)) — ftvyavAstvyavAstvamADvIhiraRyayAni cCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.175"
SUTRA_TEXT = "ऋत्व्यवास्त्व्यवास्त्वमाध्वीहिरण्ययानि च्छन्दसि"
SUTRA_DESC = "(Sandhi (euphonic combination)) — ftvyavAstvyavAstvamADvIhiraRyayAni cCandasi"


class Sutra64175:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.175: अग्निः'),
		('रामः', '', 'प.6.4.175: रामः'),
		('सीता', '', 'प.6.4.175: सीता'),
	]

