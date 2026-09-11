# Sutra प.6.3.65: इष्टकेषीकामालानां चिततूलभारिषु
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.65"
SUTRA_TEXT = "इष्टकेषीकामालानां चिततूलभारिषु"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6365:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.65: अग्निः'),
		('रामः', '', 'प.6.3.65: रामः'),
		('सीता', '', 'प.6.3.65: सीता'),
	]

