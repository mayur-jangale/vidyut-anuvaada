# Sutra प.6.3.43: घरूपकल्पचेलड्ब्रुवगोत्रमतहतेषु ङ्योऽनेकाचो ह्रस्वः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.43"
SUTRA_TEXT = "घरूपकल्पचेलड्ब्रुवगोत्रमतहतेषु ङ्योऽनेकाचो ह्रस्वः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6343:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.43: अग्निः'),
		('रामः', '', 'प.6.3.43: रामः'),
		('सीता', '', 'प.6.3.43: सीता'),
	]

