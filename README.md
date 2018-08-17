# STACK-OVERFLOW-LITE

## Project Overview
### StackOverflow-lite is a platform where people can ask questions and provide answers (( Andela challange cohort 31 ))

#### By ****Enock OMONDI****
## Description

#### It is an API that enables CRUD functionality for posting, viewing, answering, and deleting questions on the platform

## Prerequisites

* Python 3.6 or later
* flask
* Git 
* Virtualenv
* Pytest

## Development

Clone the repository:

```git clone "" ```


## Dependencies
- Install the project dependencies in the environment:
> $ pip install -r requirements.txt

## API endpoints

Test | API-endpoint | HTTP-Verb
------------ | -------------- | ------------ 
User can post a question | /api/v1/questions | POST
User can view all questions | /api/v1/questions | GET
User can view a single question | /api/v1/questions/<question_id> | GET
User can update a question | /api/v1/questions/<question_id> |PUT
User can delete a a question | /api/v1/questions/<question_id> | DELETE
User can create an account | /auth/signin | POST
User can log into the account | /auth/login | POST
User can post an answer to a question | /api/v1/questions<question_id>Answers<answer_id> | POST
User can downvote or upvote an answer to a question | /api/v1/questions<question_id>Answers<answer_id>vote?vote | POST

## Testing
Test the endpoints using Postman or curl

*this readme will be updated periodically*

## Acknowledgement

*Andela Kenya*