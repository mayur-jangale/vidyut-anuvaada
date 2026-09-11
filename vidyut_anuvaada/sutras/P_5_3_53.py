# Sutra प.5.3.53: भूतपूर्वे चरट्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — BUtapUrve caraw

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.53"
SUTRA_TEXT = "भूतपूर्वे चरट्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — BUtapUrve caraw"


class Sutra5353:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.53: अग्निः'),
		('रामः', '', 'प.5.3.53: रामः'),
		('सीता', '', 'प.5.3.53: सीता'),
	]

