# Graduation-Project
My diploma project is the development and implementation of a website designed for the exchange of posts and comments between users. On the site we can publish posts, comment and like, publish encrypted private messages, as well as an admin panel for tracking and controlling all actions. The main focus is on data security and protection from vulnerabilities

Goal and objectives:
Create a secure website and protect it from attacks.
Ensure the ability to publish messages and comments.
Introduce a private messaging system with encryption to ensure confidentiality.
Develop an administrative panel for managing users and monitoring activity.
Protect the website in accordance with Federal Law No. 149-FZ
![image](https://github.com/Elderbazy1/Graduation-Project/assets/129333030/44e8144e-fe3f-431d-b01b-3713ce007605)

Admin Page
The admin page allows you to monitor and control all activities on the site.
The administrator has the following rights:
Delete any posts and comments
Delete users
Monitor all activity on the site
This panel provides full control over content and users, helping to maintain order and security on the site.
![image](https://github.com/Elderbazy1/Graduation-Project/assets/129333030/375ba48f-78be-4a47-ad4d-6edede4c6cf1)

Private Messages:
Users can send private messages to each other in a private chat.
Each private message is visible only to the sender and recipient, making communication private.
Modern encryption algorithms are used to ensure the privacy of messages between users. This includes AES, the Advanced Encryption Standard.
![image](https://github.com/Elderbazy1/Graduation-Project/assets/129333030/5e41c1a5-5e07-462b-a9a9-49cdfa45d8dc)

A login and password are used to authenticate users. Users must enter their credentials to access the system. Passwords are stored encrypted using the bcrypt algorithm, which guarantees their security.
Access Management
Access to different parts of the site is limited based on user roles. The following roles have been implemented in the system:
User: access to the main functions of the site.
Administrator: full access to all functions and settings of the site, including management of content created by users.
![image](https://github.com/Elderbazy1/Graduation-Project/assets/129333030/e1967cad-e8ef-41ac-b8ef-9f8a3fef0179)

Tools used to protect the site
Encrypt passwords and databases
Encryption of messages between participants
Protection against Man-in-the-Middle attacks
Encryption of databases and passwords
Applied methods of password hashing and protection against leaks
Protection against vulnerabilities
Cross-site scripting (XSS)
SQL injection
Cross-site request forgery (CSRF)

