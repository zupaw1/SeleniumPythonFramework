import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver = webdriver.Chrome(
        #   executable_path="C:\\Users\\DELL\\PycharmProjects\\PythonSelFramework\\PythonSelFramework\\drivers\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # driver = webdriver.Firefox(
        #  executable_path="C:\\Users\\DELL\\PycharmProjects\\PythonSelFramework\\PythonSelFramework\\drivers\\geckodriver.exe")
    elif browser_name == "IE":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

        # driver = webdriver.Edge(
        #   executable_path="C:\\Users\\DELL\\PycharmProjects\\PythonSelFramework\\PythonSelFramework\\drivers\\msedgedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.

        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)


# it hooks for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Angular Practice Shop'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester'] = 'zpawlak'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)
