# Sutra प.1.2.43: प्रथमानिर्दिष्टं समास उपसर्जनम्
# (Samjna (technical definitions)) — praTamAnirdizwaM samAsa upasarjanam

from P_1_2 import apply_1_2_43

SUTRA_CODE = "प.1.2.43"
SUTRA_TEXT = "प्रथमानिर्दिष्टं समास उपसर्जनम्"
SUTRA_DESC = "(Samjna (technical definitions)) — praTamAnirdizwaM samAsa upasarjanam"


class Sutra1243:
	def apply(self, word, pos):
		return apply_1_2_43(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-samāsa:अग्निः'),
		('रामः', '', 'non-samāsa:रामः'),
		('सीता', '', 'non-samāsa:सीता'),
	]

