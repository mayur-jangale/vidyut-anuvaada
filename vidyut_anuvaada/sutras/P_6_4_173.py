# Sutra प.6.4.173: औक्षमनपत्ये
# (Sandhi (euphonic combination)) — Okzamanapatye

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.173"
SUTRA_TEXT = "औक्षमनपत्ये"
SUTRA_DESC = "(Sandhi (euphonic combination)) — Okzamanapatye"


class Sutra64173:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.173: अग्निः'),
		('रामः', '', 'प.6.4.173: रामः'),
		('सीता', '', 'प.6.4.173: सीता'),
	]

