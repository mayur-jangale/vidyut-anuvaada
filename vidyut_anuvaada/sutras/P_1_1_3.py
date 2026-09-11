# Sutra प.1.1.3: इको गुणवृद्धी
# Defines ik as the set of vowels {i, u, ṛ, ḷ}

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.3"
SUTRA_TEXT = "इको गुणवृद्धी"
SUTRA_DESC = "Defines ik as the set of vowels {i, u, ṛ, ḷ}"


class Sutra113:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_3
		return apply_1_1_3(word, pos)

	EXAMPLES = [
		('पितृ', '', 'ik={इ,उ,ऋ,ऌ};input=पितृ;matches='),
		('वाक्', '', 'ik={इ,उ,ऋ,ऌ};input=वाक्;matches='),
	]

