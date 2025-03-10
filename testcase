import jwt
import time
from datetime import datetime, timedelta

# Secret key for signing the JWT
SECRET_KEY = "mysecretkey"

# Function to generate a JWT token
def generate_jwt(payload):
    """
    Generate a JWT token.
    :param payload: The payload data to include in the token (usually a dictionary).
    :return: Encoded JWT token as a string.
    """
    # Adding expiration time to the payload (token expires in 1 hour)
    payload['exp'] = datetime.utcnow() + timedelta(hours=1)
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Function to decode and validate a JWT token
def validate_jwt(token):
    """
    Validate a JWT token.
    :param token: The JWT token to validate.
    :return: Decoded payload if the token is valid, else raises an error.
    """
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")

# Test Case 1: Generate a valid JWT token
def test_generate_jwt():
    print("Test Case 1: Generate JWT Token")
    user_data = {"sub": "user123", "name": "John Doe"}
    token = generate_jwt(user_data)
    
    assert token is not None, "Token should not be None"
    assert len(token.split('.')) == 3, "Token should have 3 parts"
    print(f"Generated Token: {token}")
    print("Test passed!\n")

# Test Case 2: Validate a valid JWT token
def test_validate_jwt_valid_token():
    print("Test Case 2: Validate valid JWT Token")
    user_data = {"sub": "user123", "name": "John Doe"}
    token = generate_jwt(user_data)
    
    decoded = validate_jwt(token)
    assert decoded["sub"] == "user123", "User ID should be 'user123'"
    assert decoded["name"] == "John Doe", "Name should be 'John Doe'"
    print(f"Decoded Payload: {decoded}")
    print("Test passed!\n")

# Test Case 3: Validate an expired JWT token
def test_validate_jwt_expired_token():
    print("Test Case 3: Validate expired JWT Token")
    # Create an expired token
    user_data = {"sub": "user123", "name": "John Doe", "exp": datetime.utcnow() - timedelta(seconds=1)}
    expired_token = jwt.encode(user_data, SECRET_KEY, algorithm="HS256")
    
    try:
        validate_jwt(expired_token)
        print("Test failed: Token should be expired")
    except Exception as e:
        assert str(e) == "Token has expired", "Error message should indicate expired token"
        print("Test passed!\n")

# Test Case 4: Validate a token with an invalid signature
def test_validate_jwt_invalid_signature():
    print("Test Case 4: Validate JWT Token with Invalid Signature")
    user_data = {"sub": "user123", "name": "John Doe"}
    valid_token = generate_jwt(user_data)
    
    # Alter the token to make the signature invalid
    invalid_token = valid_token[:-1] + 'X'  # Modify the last character of the token
    
    try:
        validate_jwt(invalid_token)
        print("Test failed: Token should be invalid due to signature mismatch")
    except Exception as e:
        assert str(e) == "Invalid token", "Error message should indicate invalid token"
        print("Test passed!\n")

# Test Case 5: Handle missing token
def test_missing_jwt_token():
    print("Test Case 5: Handle missing JWT Token")
    try:
        validate_jwt(None)
        print("Test failed: Token should not be None")
    except Exception as e:
        assert str(e) == "Invalid token", "Error message should indicate invalid token"
        print("Test passed!\n")

# Run the tests
test_generate_jwt()
test_validate_jwt_valid_token()
test_validate_jwt_expired_token()
test_validate_jwt_invalid_signature()
test_missing_jwt_token()
