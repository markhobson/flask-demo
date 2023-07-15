def test_index(client):
    response = client.get("/")
    assert b"<p>['a', 'b', 'c']</p>" in response.data
