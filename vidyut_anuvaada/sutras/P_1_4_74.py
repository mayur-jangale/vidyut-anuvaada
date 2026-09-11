# Sutra प.1.4.74: साक्षात्प्रभृतीनि च
# (Samjna (technical definitions)) — sAkzAtpraBftIni ca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.74"
SUTRA_TEXT = "साक्षात्प्रभृतीनि च"
SUTRA_DESC = "(Samjna (technical definitions)) — sAkzAtpraBftIni ca"


class Sutra1474:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_74
		return apply_1_4_74(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-sAkzAt:अग्निः'),
		('रामः', '', 'not-sAkzAt:रामः'),
		('सीता', '', 'not-sAkzAt:सीता'),
	]

