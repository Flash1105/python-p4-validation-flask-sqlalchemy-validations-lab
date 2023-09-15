import pytest
from sqlalchemy.exc import IntegrityError, CompileError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app import app
from models import db, Author, Post


class TestAuthor:
    '''Class Author in models.py'''

    def test_requires_name(self):
        '''requires each record to have a name.'''

        

    def test_requires_unique_name(self):
        '''requires each record to have a unique name.'''
   


    def test_requires_ten_digit_phone_number(self):
        '''requires each phone number to be exactly ten digits.'''

  

class TestPost:
    '''Class Post in models.py'''

    def test_requires_title(self):
        '''requires each post to have a title.'''

      
    def test_content_length(self):
        '''requires content to be greater than or equal 250 characters long.'''

 

    def test_content_length(self):
        '''Content too short test. Less than 250 chars.'''

    

    def test_summary_length(self):
        '''Summary too long test. More than 250 chars.'''

      

    def test_category(self):
        '''Incorrect category test'''

       

    def test_clickbait(self):
        '''Test clickbait validator for title.'''
       
            
