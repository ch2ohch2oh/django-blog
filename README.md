# Blog Site using Django

Building a blog is not a novel idea. 
THis project is mostly the result of following
Corey Schader's amazing [Django tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p).

Bootstrap4 is used for the front-end display. 
Backend is handled by django. `django-crispy-form` is used
to make the forms look better. 

`nginx` is used as our reverse proxy. It serves static files
and media files to the client directly. For web requests, 
it is forwarded to `gunicorn` which forward the request
to `django`.

Finally, the whole application is packaged with `docker`.
For the production environment, we have 3 containers 
in total for `nginx`, `gunicorn` and `postgres`.
