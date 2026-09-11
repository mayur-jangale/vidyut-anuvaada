# Sutra प.6.4.174: दाण्डिनायनहास्तिनायनाथर्वणिकजैह्माशिनेयवाशिनायनिभ्रौणहत्यधैवत्यसारवैक्ष्वाकमैत्रेयहिरण्मयानि
# (Sandhi (euphonic combination)) — dARqinAyanahAstinAyanATarvaRikajEhmASineyavASinAyaniBrORahatyaDEvatyasAravEkzvAkamEtreyahiraRmayAni

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.174"
SUTRA_TEXT = "दाण्डिनायनहास्तिनायनाथर्वणिकजैह्माशिनेयवाशिनायनिभ्रौणहत्यधैवत्यसारवैक्ष्वाकमैत्रेयहिरण्मयानि"
SUTRA_DESC = "(Sandhi (euphonic combination)) — dARqinAyanahAstinAyanATarvaRikajEhmASineyavASinAyaniBrORahatyaDEvatyasAravEkzvAkamEtreyahiraRmayAni"


class Sutra64174:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.174: अग्निः'),
		('रामः', '', 'प.6.4.174: रामः'),
		('सीता', '', 'प.6.4.174: सीता'),
	]

