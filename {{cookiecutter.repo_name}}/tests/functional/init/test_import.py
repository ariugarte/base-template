from pytest_bdd import scenario, when, then  

@scenario('test_import.feature', 'Import the {{ cookiecutter.project_slug }} package successfully')  
def test_import_{{ cookiecutter.project_slug }}():
    """Test importing the {{ cookiecutter.project_slug }} package."""
    pass
  
@when('I import the {{ cookiecutter.project_slug }} package', target_fixture="{{ cookiecutter.project_slug }}_module")
def ca007_module_import():
    """Import the {{ cookiecutter.project_slug }} package."""
    import {{ cookiecutter.project_slug }}
    return {{ cookiecutter.project_slug }}
    
@then('I should be able to access its __version__ attribute')
def check_version({{ cookiecutter.project_slug }}_module):
    """Check that the __version__ attribute exists."""
    assert hasattr({{ cookiecutter.project_slug }}_module, '__version__')
    assert isinstance({{ cookiecutter.project_slug }}_module.__version__, str)