# Sutra प.6.3.40: स्वाङ्गाच्चेतोऽमानिनि
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.40"
SUTRA_TEXT = "स्वाङ्गाच्चेतोऽमानिनि"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6340:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.40: अग्निः'),
		('रामः', '', 'प.6.3.40: रामः'),
		('सीता', '', 'प.6.3.40: सीता'),
	]

