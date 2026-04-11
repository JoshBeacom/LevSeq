from levseq import seqfit


def test_seqfit_module_imports_without_optional_esm_dependencies():
    assert hasattr(seqfit, "gen_seqfitvis")
