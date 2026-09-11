# Sutra प.8.1.69: कुत्सने च सुप्यगोत्रादौ
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.69"
SUTRA_TEXT = "कुत्सने च सुप्यगोत्रादौ"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8169:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.69: अग्निः'),
		('रामः', '', 'प.8.1.69: रामः'),
		('सीता', '', 'प.8.1.69: सीता'),
	]

