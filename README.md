# User Activity 
This is a user activity API which gives a JSON response of users activity

Live demo:
   * 1.Restful GET API:https://useractivityapi.herokuapp.com/userlist/

Technology Used:
   * 1.Django Rest Framework
   * 2.SQLite

Models:
   * 1.User
   * 2.Activity Period

User has a many-to-many relationship with ActivityPeriod.

Dummy data is populated in database by using a custom command i.e.  python manage.py update_data  
