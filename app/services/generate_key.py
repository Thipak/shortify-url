from app import db
from app.models.urls import URL

def generate_key(url):
    """
    Generate a unique key for the given URL.
    """
    # Check if the URL already exists in the database
    existing_url = URL.query.filter_by(url=url).first()
    
    if existing_url:
        # If it exists, return the existing key
        return existing_url.id  # Assuming id is used as the key
    
    # If it doesn't exist, create a new entry in the database
    # Generate a unique key (this could be a hash, random string, etc.)
    id = random_string(10)  # Example: generate a random string of length 10
    while URL.query.filter_by(id=id).first() is not None:
        id = random_string(10)  # Ensure uniqueness
    new_url = URL(id=id, url=url)
    db.session.add(new_url)
    db.session.commit()
    
    return new_url.id  # Return the newly created key

def random_string(length):
    """
    Generate a random string of fixed length.
    """
    import random
    import string
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))