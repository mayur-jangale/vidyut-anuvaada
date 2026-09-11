# Sutra प.6.1.154: मस्करमस्करिणौ वेणुपरिव्राजकयोः
# sandhi-sūtra प.6.1.154

from P_6_1 import apply_6_1_154

SUTRA_CODE = "प.6.1.154"
SUTRA_TEXT = "मस्करमस्करिणौ वेणुपरिव्राजकयोः"
SUTRA_DESC = "sandhi-sūtra प.6.1.154"


class Sutra61154:
	def apply(self, word, pos):
		return apply_6_1_154(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.154:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.154:marker=padartha;input=रामः'),
		('सीता', '', '6.1.154:marker=padartha;input=सीता'),
	]
