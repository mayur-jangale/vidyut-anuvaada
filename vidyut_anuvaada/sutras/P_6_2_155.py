# Sutra प.6.2.155: नञो गुणप्रतिषेधे सम्पाद्यर्हहितालमर्थास्तद्धिताः
# (Sandhi (euphonic combination)) — naYo guRapratizeDe sampAdyarhahitAlamarTAstadDitAH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.155"
SUTRA_TEXT = "नञो गुणप्रतिषेधे सम्पाद्यर्हहितालमर्थास्तद्धिताः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — naYo guRapratizeDe sampAdyarhahitAlamarTAstadDitAH"


class Sutra62155:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.155: अग्निः'),
		('रामः', '', 'प.6.2.155: रामः'),
		('सीता', '', 'प.6.2.155: सीता'),
	]

