# Sutra प.1.4.105: युष्मद्युपपदे समानाधिकरणे स्थानिन्यपि मध्यमः
# (Samjna (technical definitions)) — yuzmadyupapade samAnADikaraRe sTAninyapi maDyamaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.105"
SUTRA_TEXT = "युष्मद्युपपदे समानाधिकरणे स्थानिन्यपि मध्यमः"
SUTRA_DESC = "(Samjna (technical definitions)) — yuzmadyupapade samAnADikaraRe sTAninyapi maDyamaH"


class Sutra14105:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_105
		return apply_1_4_105(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-yusmad-maDyama:अग्निः'),
		('रामः', '', 'not-yusmad-maDyama:रामः'),
		('सीता', '', 'not-yusmad-maDyama:सीता'),
	]

