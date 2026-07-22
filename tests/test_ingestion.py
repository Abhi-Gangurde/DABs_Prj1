def clean_room_names(columns):
    return [c.strip().lower().replace(" ", "_") for c in columns]

def test_clean_room_names():
    raw = ["Customer ID", "First Name", "Last Name"]
    expected = ["customer_id", "first_name", "last_name"]
    assert clean_room_names(raw) == expected
    