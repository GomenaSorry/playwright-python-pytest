### Design:
This is a simple demo automated tests using the Playwright Test Framework and Python. 

Following the Page Object Model (POM) design pattern, Page Object Classes are created based on the application's web pages. Each Page Object Class contains web elements as class properties, which are initialized when the Page Object Class is instantiated. The class methods define actions to interact with these elements. Most of the locators are initialized using Playwright's 'get_by_role()' method, specifying the role and using the 'name' argument to search for the element's text content. This approach also validates if the element has the correct role.

The test classes contain tests related to the page under test. Using the concept of test fixtures and pytest.fixtures, Page Object Classes are instantiated as arguments in the test methods, automatically constructing them when the test method is executed. This approach reduces the redundancy of manual object creation. The fixture logic is located in 'tests/conftest.py'. Additionally, there is a sample of parameterized tests in tests/'test_product_details.py', demonstrating pytest's capability to run a test using a set of test data. The tests can also be executed in parallel using the pytest-xdist plugin.

Test reporting is handled by the Allure Reporter plugin, with annotations on each test to organize them by epic, feature, and story. Screenshots are generated whenever a test fails and are attached to the Allure HTML Report. This functionality is enabled by custom code located in 'tests/conftest.py'.

### Installation:
1. Create a virtual environment to manage packages locally:
    
    > python3 -m venv .venv

2. Activate virtual environment:
    
    > .venv/Scripts/activate

3. Install dependencies using requirements.txt:
   
   > pip3install -r requirements.txt

    --or--

    Install individually:

    Playwright

    > pip3 install playwright

    pytest

   > pip3 install pytest

    pytest-playwright

   > pip3 install pytest-playwright

    allure-pytest

   > pip3 install pytest-playwright

    pytest-xdist

   > pip3 install pytest-xdist

    flask
    
   > pip3 install flask

### Running tests (using VSCode)
1. Ensure that the app is running by opening a separate terminal:
   > cd store
   > python app.py

2. Run tests

    a. using pytest and Allure Reporter:

    > pytest --alluredir='test-results'

    b. using pytest, Allure Reporter and parallel execution:

    > pytest --alluredir='test-results' -n [number of workers]

3. Generate Allure HTML Report:

   > allure serve 'test-results'






