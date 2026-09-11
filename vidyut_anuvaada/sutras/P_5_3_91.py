# Sutra प.5.3.91: वत्सोक्षाश्वर्षभेभ्यश्च तनुत्वे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vatsokzASvarzaBeByaSca tanutve

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.91"
SUTRA_TEXT = "वत्सोक्षाश्वर्षभेभ्यश्च तनुत्वे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vatsokzASvarzaBeByaSca tanutve"


class Sutra5391:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.91: अग्निः'),
		('रामः', '', 'प.5.3.91: रामः'),
		('सीता', '', 'प.5.3.91: सीता'),
	]

