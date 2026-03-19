# Login Vulnerability Lab

## Description
A simple vulnerable login system built using Python and HTML to demonstrate authentication weaknesses and basic web security concepts.

## Features
- Basic login form (HTML)
- Python-based backend server
- Hardcoded authentication logic
- Designed for security testing

## Tools Used
- Python (HTTP server)
- HTML
- Burp Suite (for request interception)

## Vulnerability
The login system uses insecure authentication logic:
- Hardcoded credentials
- No input validation
- No protection against manipulation

## What I Learned
- How HTTP requests work (GET/POST)
- How login systems handle authentication
- How to intercept and modify requests using Burp Suite
- Basics of web security vulnerabilities

## Ethical Note
This project is created for educational purposes only. All testing was performed in a controlled local environment.

## Future Improvements
- Introduce SQL Injection vulnerability
- Implement secure authentication methods
- Add password hashing
