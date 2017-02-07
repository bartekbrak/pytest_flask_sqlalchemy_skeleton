# pytest + flask + sqlalchemy working skeleton

We had this problem where we created a flask app prototype without tests quickly.
When we got to writing tests I had a problem to figure out how to setup py.test so that
it rolls back transaction after every test. Our specific setup didn't use app factory and did
some other things in such a way that I couldn't use recipes on the Internet.

I'm documenting the solution as I have a feeling I will be in this situation again.

