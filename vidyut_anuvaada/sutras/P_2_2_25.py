# Sutra प.2.2.25: संख्ययाऽव्ययासन्नादूराधिकसंख्याः संख्येये
# (Samasa (compound formation)) — saMKyayA'vyayAsannAdUrADikasaMKyAH saMKyeye

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.25"
SUTRA_TEXT = "संख्ययाऽव्ययासन्नादूराधिकसंख्याः संख्येये"
SUTRA_DESC = "(Samasa (compound formation)) — saMKyayA'vyayAsannAdUrADikasaMKyAH saMKyeye"


class Sutra2225:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

