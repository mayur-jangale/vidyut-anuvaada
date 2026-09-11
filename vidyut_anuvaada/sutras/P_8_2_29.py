# Sutra प.8.2.29: स्कोः संयोगाद्योरन्ते च
# ṣaṇṇāṃ luk — elision of six suffixes (ṣaṇṇāṃ luk)

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.29"
SUTRA_TEXT = "स्कोः संयोगाद्योरन्ते च"
SUTRA_DESC = "ṣaṇṇāṃ luk — elision of six suffixes (ṣaṇṇāṃ luk)"


class Sutra8229:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.29: अग्निः'),
		('रामः', '', 'प.8.2.29: रामः'),
		('सीता', '', 'प.8.2.29: सीता'),
	]

