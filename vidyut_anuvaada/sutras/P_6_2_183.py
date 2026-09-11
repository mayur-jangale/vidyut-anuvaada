# Sutra प.6.2.183: प्रादस्वाङ्गं संज्ञायाम्
# (Sandhi (euphonic combination)) — prAdasvANgaM saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.183"
SUTRA_TEXT = "प्रादस्वाङ्गं संज्ञायाम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — prAdasvANgaM saMjYAyAm"


class Sutra62183:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.183: अग्निः'),
		('रामः', '', 'प.6.2.183: रामः'),
		('सीता', '', 'प.6.2.183: सीता'),
	]

