# Sutra प.2.4.83: नाव्ययीभावादतोऽम्त्वपञ्चम्याः
# (Samasa (compound formation)) — nAvyayIBAvAdato'mtvapaYcamyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.83"
SUTRA_TEXT = "नाव्ययीभावादतोऽम्त्वपञ्चम्याः"
SUTRA_DESC = "(Samasa (compound formation)) — nAvyayIBAvAdato'mtvapaYcamyAH"


class Sutra2483:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

