def test_login(sample_data):
    print(f"Testing login for {sample_data['user']} with role {sample_data['role']}")
    print(sample_data["user"])
    assert sample_data["role"] == "Admin"
