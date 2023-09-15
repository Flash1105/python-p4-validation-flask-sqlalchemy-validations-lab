from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import datetime

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String, nullable=False)

    @validates('phone_number')
    def validate_phone_number(self, key, value):
        if len(value) != 10:
            raise ValueError("Phone number must be exactly ten digits.")
        return value

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)

    @validates('content')
    def validate_content_length(self, key, value):
        if len(value) < 250:
            raise ValueError("Content must be at least 250 characters long.")
        return value

    @validates('summary')
    def validate_summary_length(self, key, value):
        if value and len(value) > 250:  # Check if summary is provided before validating its length
            raise ValueError("Summary can't be more than 250 characters long.")
        return value

    @validates('category')
    def validate_category(self, key, value):
        valid_categories = ['Non-Fiction', 'Fiction', 'Science', 'Technology', 'Politics', 'Education']
        if value not in valid_categories:
            raise ValueError("Invalid category.")
        return value

    @validates('title')
    def validate_clickbait(self, key, value):
        if "clickbait" in value.lower():
            raise ValueError("Title cannot contain the word 'clickbait'.")
        return value
