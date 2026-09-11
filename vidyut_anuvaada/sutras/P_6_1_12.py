# Sutra प.6.1.12: दाश्वान् साह्वान् मीढ्वांश्च
# sandhi-sūtra प.6.1.12

from P_6_1 import apply_6_1_12

SUTRA_CODE = "प.6.1.12"
SUTRA_TEXT = "दाश्वान् साह्वान् मीढ्वांश्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.12"


class Sutra6112:
	def apply(self, word, pos):
		return apply_6_1_12(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.12:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.12:marker=padartha;input=रामः'),
		('सीता', '', '6.1.12:marker=padartha;input=सीता'),
	]
