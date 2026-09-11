# Sutra प.3.4.65: शकधृषज्ञाग्लाघटरभलभक्रमसहार्हास्त्यर्थेषु तुमुन्
# rvul — agent noun suffix (kāraka-type)

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.65"
SUTRA_TEXT = "शकधृषज्ञाग्लाघटरभलभक्रमसहार्हास्त्यर्थेषु तुमुन्"
SUTRA_DESC = "rvul — agent noun suffix (kāraka-type)"


class Sutra3465:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

