from src.main import get_ip

def test_get_ip():
    ip = get_ip()
    assert isinstance(ip, str)