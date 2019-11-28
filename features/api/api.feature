Feature: Metis API
  In order to access data from various information systems,
  as a web application
  I need REST based API to get, save and delete data
  and perform other operations

    Scenario:
      Given that a user must log on
      When the user provides a username and password
      And the username and password are passed to the authentication service
      Then the service should pass pass a JWT token
