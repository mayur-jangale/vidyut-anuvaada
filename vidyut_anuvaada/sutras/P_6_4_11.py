# Sutra प.6.4.11: अप्तृन्तृच्स्वसृनप्तृनेष्टृत्वष्टृक्षत्तृहोतृपोतृप्रशास्तॄणाम्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.11"
SUTRA_TEXT = "अप्तृन्तृच्स्वसृनप्तृनेष्टृत्वष्टृक्षत्तृहोतृपोतृप्रशास्तॄणाम्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6411:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.11: अग्निः'),
		('रामः', '', 'प.6.4.11: रामः'),
		('सीता', '', 'प.6.4.11: सीता'),
	]

