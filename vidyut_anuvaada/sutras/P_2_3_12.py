# Sutra प.2.3.12: गत्यर्थकर्मणि द्वितीयाचतुर्थ्यौ चेष्टायामनध्वनि
# (Samasa (compound formation)) — gatyarTakarmaRi dvitIyAcaturTyO cezwAyAmanaDvani

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.12"
SUTRA_TEXT = "गत्यर्थकर्मणि द्वितीयाचतुर्थ्यौ चेष्टायामनध्वनि"
SUTRA_DESC = "(Samasa (compound formation)) — gatyarTakarmaRi dvitIyAcaturTyO cezwAyAmanaDvani"


class Sutra2312:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

