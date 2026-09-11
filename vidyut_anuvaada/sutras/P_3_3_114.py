# Sutra प.3.3.114: नपुंसके भावे क्तः
# kṛdavyayibhāva — kṛdanta as avyaya

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.114"
SUTRA_TEXT = "नपुंसके भावे क्तः"
SUTRA_DESC = "kṛdavyayibhāva — kṛdanta as avyaya"


class Sutra33114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

