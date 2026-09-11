# Sutra प.6.2.156: ययतोश्चातदर्थे
# (Sandhi (euphonic combination)) — yayatoScAtadarTe

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.156"
SUTRA_TEXT = "ययतोश्चातदर्थे"
SUTRA_DESC = "(Sandhi (euphonic combination)) — yayatoScAtadarTe"


class Sutra62156:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.156: अग्निः'),
		('रामः', '', 'प.6.2.156: रामः'),
		('सीता', '', 'प.6.2.156: सीता'),
	]

