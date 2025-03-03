Feature: Import {{ cookiecutter.project_slug }} package  
  
  Scenario: Import the {{ cookiecutter.project_slug }} package successfully  
    When I import the {{ cookiecutter.project_slug }} package  
    Then I should be able to access its __version__ attribute  