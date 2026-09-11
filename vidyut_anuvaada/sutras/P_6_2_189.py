# Sutra प.6.2.189: अनोरप्रधानकनीयसी
# (Sandhi (euphonic combination)) — anorapraDAnakanIyasI

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.189"
SUTRA_TEXT = "अनोरप्रधानकनीयसी"
SUTRA_DESC = "(Sandhi (euphonic combination)) — anorapraDAnakanIyasI"


class Sutra62189:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.189: अग्निः'),
		('रामः', '', 'प.6.2.189: रामः'),
		('सीता', '', 'प.6.2.189: सीता'),
	]

