import pytest

from backend.services.document_service import DocumentService, _flatten_dict


def test_flatten_dict_preserves_nested_template_keys():
    assert _flatten_dict({"participant": {"name": "Asha"}}) == {
        "participant.name": "Asha"
    }


@pytest.mark.parametrize("filename", ["../outside", "nested/file", ""])
def test_generate_docx_rejects_path_traversal_names(filename, tmp_path):
    service = DocumentService()
    service.base_output = str(tmp_path)

    with pytest.raises(ValueError, match="simple DOCX name"):
        service.generate_docx_from_template("missing.docx", {}, filename)
