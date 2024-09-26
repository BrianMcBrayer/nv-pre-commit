import pytest
from pre_commit_hooks.detect_nv_keys import check_file_contents


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("No keys here", []),
        ("nvapi-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_-", ["nvap******Z_-"]),
        ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwx", ["abcd******tuv"]),
        (
            "nvapi-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_- and abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwx",
            ["nvap******Z_-", "abcd******tuv"],
        ),
        ("Invalid key: nvapi-tooshort", []),
        (
            "Invalid key: toolongabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz",
            ["tool******mno"],
        ),
    ],
)
def test_check_file_contents(input_text, expected_output):
    assert check_file_contents(input_text) == expected_output


def test_check_file_contents_with_multiple_keys():
    input_text = """
    Here's a PAT: nvapi-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_-
    And here's an API key: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwx
    Another PAT: nvapi-ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_-
    """
    expected_output = ["nvap******Z_-", "nvap******z_-", "abcd******tuv"]
    assert set(check_file_contents(input_text)) == set(expected_output)


def test_check_file_contents_with_no_keys():
    input_text = "This is a text without any valid keys."
    assert check_file_contents(input_text) == []


def test_check_file_contents_with_invalid_keys():
    input_text = """
    Invalid PAT: nvapi-tooshort
    Invalid API key: toolongabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz
    """
    assert check_file_contents(input_text) == ["tool******mno"]
