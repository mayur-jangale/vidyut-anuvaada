from mayur import freq


def test_counts_nonnegative_and_unknown_zero():
    assert freq.form_count("zzzz-not-a-form") == 0
    assert freq.lemma_count("zzzz-not-a-lemma") == 0
    assert freq.total_tokens() >= 0


def test_known_form_if_table_present():
    if freq.total_tokens() == 0:
        return
    assert freq.form_count("rAmas") > 100
    assert freq.lemma_count("rAma") > 100
    assert freq.total_tokens() > 100000
