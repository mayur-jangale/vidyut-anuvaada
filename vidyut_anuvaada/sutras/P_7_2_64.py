# Sutra प.7.2.64: बभूथाततन्थजगृम्भववर्थेति निगमे
# (Taddhita (secondary derivations)) — baBUTAtatanTajagfmBavavarTeti nigame

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.64"
SUTRA_TEXT = "बभूथाततन्थजगृम्भववर्थेति निगमे"
SUTRA_DESC = "(Taddhita (secondary derivations)) — baBUTAtatanTajagfmBavavarTeti nigame"


class Sutra7264:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.64: अग्निः'),
		('रामः', '', 'प.7.2.64: रामः'),
		('सीता', '', 'प.7.2.64: सीता'),
	]

