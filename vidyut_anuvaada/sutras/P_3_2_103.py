# Sutra प.3.2.103: सुयजोर्ङ्वनिप्
# ktavatu — active past participle suffix ('having done')

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.103"
SUTRA_TEXT = "सुयजोर्ङ्वनिप्"
SUTRA_DESC = "ktavatu — active past participle suffix ('having done')"


class Sutra32103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

