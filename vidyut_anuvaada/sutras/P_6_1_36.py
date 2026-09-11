# Sutra प.6.1.36: अपस्पृधेथामानृचुरानृहुश्चिच्युषेतित्याजश्राताःश्रितमाशीराशीर्त्ताः
# sandhi-sūtra प.6.1.36

from P_6_1 import apply_6_1_36

SUTRA_CODE = "प.6.1.36"
SUTRA_TEXT = "अपस्पृधेथामानृचुरानृहुश्चिच्युषेतित्याजश्राताःश्रितमाशीराशीर्त्ताः"
SUTRA_DESC = "sandhi-sūtra प.6.1.36"


class Sutra6136:
	def apply(self, word, pos):
		return apply_6_1_36(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.36:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.36:marker=padartha;input=रामः'),
		('सीता', '', '6.1.36:marker=padartha;input=सीता'),
	]
