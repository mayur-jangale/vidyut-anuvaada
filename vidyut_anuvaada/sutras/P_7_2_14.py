# Sutra प.7.2.14: श्वीदितो निष्ठायाम्
# (Taddhita (secondary derivations)) — SvIdito nizWAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.14"
SUTRA_TEXT = "श्वीदितो निष्ठायाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — SvIdito nizWAyAm"


class Sutra7214:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.14: अग्निः'),
		('रामः', '', 'प.7.2.14: रामः'),
		('सीता', '', 'प.7.2.14: सीता'),
	]

