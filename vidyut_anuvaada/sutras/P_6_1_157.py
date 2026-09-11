# Sutra प.6.1.157: पारस्करप्रभृतीनि च संज्ञायाम्
# sandhi-sūtra प.6.1.157

from P_6_1 import apply_6_1_157

SUTRA_CODE = "प.6.1.157"
SUTRA_TEXT = "पारस्करप्रभृतीनि च संज्ञायाम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.157"


class Sutra61157:
	def apply(self, word, pos):
		return apply_6_1_157(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.157:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.157:marker=padartha;input=रामः'),
		('सीता', '', '6.1.157:marker=padartha;input=सीता'),
	]
