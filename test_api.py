import requests

BASE_URL = 'http://localhost:5000'

def test_register_and_login():
    # Register
    res = requests.post(f'{BASE_URL}/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    print('Register:', res.status_code, res.json())

    # Login
    res = requests.post(f'{BASE_URL}/login', json={
        'username': 'testuser',
        'password': 'password123'
    })
    print('Login:', res.status_code, res.json())

if __name__ == '__main__':
    test_register_and_login()
