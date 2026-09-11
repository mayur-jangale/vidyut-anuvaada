# Sutra प.6.3.139: सम्प्रसारणस्य
# (Sandhi (euphonic combination)) — samprasAraRasya

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.139"
SUTRA_TEXT = "सम्प्रसारणस्य"
SUTRA_DESC = "(Sandhi (euphonic combination)) — samprasAraRasya"


class Sutra63139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.139: अग्निः'),
		('रामः', '', 'प.6.3.139: रामः'),
		('सीता', '', 'प.6.3.139: सीता'),
	]

