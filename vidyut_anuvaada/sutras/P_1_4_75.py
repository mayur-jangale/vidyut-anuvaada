# Sutra प.1.4.75: अनत्याधान उरसिमनसी
# (Samjna (technical definitions)) — anatyADAna urasimanasI

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.75"
SUTRA_TEXT = "अनत्याधान उरसिमनसी"
SUTRA_DESC = "(Samjna (technical definitions)) — anatyADAna urasimanasI"


class Sutra1475:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_75
		return apply_1_4_75(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-uraH-manas:अग्निः'),
		('रामः', '', 'not-uraH-manas:रामः'),
		('सीता', '', 'not-uraH-manas:सीता'),
	]

