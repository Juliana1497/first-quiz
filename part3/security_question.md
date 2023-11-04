A01:2021 – Access Control Loss: Verify in the backend code developed for the website and the application, both in the web interface and the application, whether it specifies roles and the permissions to which each user role has access. Ensure that only a superadministrator has access to register their employees. Check if the routes assigned to each web window are secure. Confirm whether permissions are disabled when the user logs out. Determine who has access to the SQL databases.

A02:2021 – Cryptographic Flaws: Check if the passwords required for each user upon registration are secure and strong. Determine the protocol used by the website, verify the cryptographic protocol and algorithm employed by the page, examine the web address headers, check the hash function used, and confirm whether hashing is applied and if the information is stored hashed in the database.

A03:2021 – Injection: I would conduct code testing using pytest to ensure that database queries are executed correctly without compromising the integrity of the queries.

A04:2021 – Insecure Design: Verify if the application and website design include insecure methods of authenticating and storing customers' personal data. Check if the way orders are processed is vulnerable to automated processes.

A05:2021 – Incorrect Security Configuration: With the assistance of my technical team, I would verify if the permissions in AWS are correctly configured. I'll ensure there are no unnecessary functions on the website, and that error messages do not display confidential information. Additionally, I will confirm that the FastAPI configuration is secure.

A06:2021 – Vulnerable and Outdated Components: I will check the versions of software, operating systems, web/application servers, database management systems (DBMS), applications, APIs, and all components, as well as runtime environments and libraries. I will test the updated libraries for security.

A07:2021 – Identification and Authentication Failures: Validate if there is protection against automated attacks. Ensure that strong passwords are required during registration and determine the password recovery system. Check if passwords are hashed efficiently and confirm that the session identifier is not visible in the URL. Evaluate the effectiveness of logout invalidation.

A08:2021 – Software and Data Integrity Failures: Ensure that integrity verification is not skipped during application updates and implement a third-party component analysis tool.

A09:2021 – Registration and Monitoring Failures: Ensure the presence of a logging system for login failures and API errors. Verify that the logs stored in the database are monitored, and applications can detect, escalate, or alert about active attacks in real-time or near-real-time.

A10:2021 – Server-Side Request Forgery (SSRF) Attacks: Prevent users from entering URLs without validating their security. Implement "deny by default" firewall policies or network access control rules to block all intranet traffic except for essential communication.