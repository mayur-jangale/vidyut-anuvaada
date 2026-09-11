# Sutra प.6.2.193: प्रतेरंश्वादयस्तत्पुरुषे
# (Sandhi (euphonic combination)) — prateraMSvAdayastatpuruze

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.193"
SUTRA_TEXT = "प्रतेरंश्वादयस्तत्पुरुषे"
SUTRA_DESC = "(Sandhi (euphonic combination)) — prateraMSvAdayastatpuruze"


class Sutra62193:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.193: अग्निः'),
		('रामः', '', 'प.6.2.193: रामः'),
		('सीता', '', 'प.6.2.193: सीता'),
	]

