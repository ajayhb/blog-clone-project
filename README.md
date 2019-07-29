# blog-clone-project
It's a full stack website that has been built using HTML, CSS, Javascript (Medium API), Django and SQLite3.
Built it in lower environment for now. Django Version is 2.1 (since I do have both Class based views and functional views in my views.py).
"mysite" is the project name and the blog inside the folder "mysite" is the application name.
So to run the command in a lower environment (using django 2.1): type:                                                                python manage.py runserver (make sure to be inside "mysite" directory).
In this project, only the superuser can write a blog and the rest can see and comment. 
After anyone comments, their changes will not be reflected because it goes to superuser for approval.
Users can see only those comments on blogs which are approved by the Superuser.
In Superuser mode: You can create posts, publish them to move them from "Drafts" section to Main Page.
Users can see only main page and not the Drafts section.
Drafts section contains "created date" and "text" fields whereas MainPage contains "PostList View, Published date and Comments count".
