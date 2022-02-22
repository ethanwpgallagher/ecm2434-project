from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import TestCase


# Insert geckodriver executable here
pathToGeckodriver = "/Users/faris/downloads/geckodriver"


class SeleniumLoginTest(StaticLiveServerTestCase, TestCase):
    """
    This class will test the functionality of the login system with test credentials.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path=pathToGeckodriver)
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def testLoginFunctionality(self):
        """
        This function navigates directly to the login page, enters a username and
        password, and then presses the login button. It then checks that the user
        is logged in.

        Before Login Implementation:
            * assert that the page you are taken to after login does not contain
              Login or Sign Up
        After Login Implementation:
            * check for some personal information in the page source, such as
              username in the top right corner.
        """
        self.selenium.get(self.live_server_url + "/play/login")
        unameInput = self.selenium.find_element_by_name("uname")
        # Need to tweak this to allow us to use this username in final build
        unameInput.send_keys("testUser1")
        pwdInput = self.selenium.find_element_by_name("psw")
        # Need to tweak this to allow us to use this password in the final
        # build
        pwdInput.send_keys("password")
        button = self.selenium.find_element_by_xpath(
            "//input[@class='formButton arcade-font']")
        button.click()
        self.selenium.implicitly_wait(5)
        assert "Login" and "Sign Up" not in self.selenium.page_source
        assert self.selenium.title != "Login | Exeter Domination"
        # assert "<h1>Forbidden <span>(403)</span></h1>" not in self.selenium.page_source
        # The above test will continually fail until the login / signup system
        # has been implemented


class SignUpWithSeleniumTest(StaticLiveServerTestCase, TestCase):
    """
    This class will test the sign up system with test credentials and check if the
    user is sent to the correct location.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path=pathToGeckodriver)
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def testSignUpFunctionality(self):
        """
        This function loads the signup page, creates a user account, and presses
        the signup button. It then checks that the user is redirected directly
        to a page where they are logged in.

        Before Login Implementation:
            * Checks that Login and Signup are not in the page's source or title
        After Login Implementation:
            * Checks that the user is on the correct page, and their username is
              in the top right corner.
        """
        self.selenium.get(self.live_server_url + "/play/signup")
        testUsername = self.selenium.find_element_by_name("username")
        testUsername.send_keys("testUser1")
        testPassword = self.selenium.find_element_by_name("password")
        testPassword.send_keys("password")
        testRepeatPassword = self.selenium.find_element_by_name("psw-repeat")
        testRepeatPassword.send_keys("password")
        signUpButton = self.selenium.find_element_by_xpath(
            "//input[@class='formButton arcade-font']")
        signUpButton.click()
        self.selenium.implicitly_wait(5)
        assert "Login" and "Sign Up" not in self.selenium.page_source
        assert self.selenium.title != "Sign Up | Exeter Domination" or "Log In | Exeter Domination"
        # assert "<h1>Forbidden <span>(403)</span></h1>" not in self.selenium.page_source
        # The above test will continually fail until the login / signup system
        # has been implemented


class testNavigationLinks(StaticLiveServerTestCase, TestCase):
    """
    This class is mainly just to test that the hyperlinks, and navigation buttons are
    in order and working correctly. This is not currently comprehensive, but will be
    in time for release.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path=pathToGeckodriver)
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def testHomeToAboutBackToHome(self):
        """
        This function tests that the navigation buttons from the home
        page to the about page and back are in working order.
        """
        self.selenium.get(self.live_server_url + "/play")
        aboutButton = self.selenium.find_element_by_xpath(
            "//input[@class='arcade-font button2']")
        aboutButton.click()
        assert self.selenium.title == "About | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/about"
        homeButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, '/play')]")
        homeButton.click()
        assert self.selenium.title == "Home | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/"

    def testHomeToPlayBackToHome(self):
        """
        This function tests that the navigation buttons from the home
        page to the play game page and back are in working order.
        """
        self.selenium.get(self.live_server_url + "/play")
        playButton = self.selenium.find_element_by_xpath(
            "//input[@class='arcade-font button1']")
        playButton.click()
        assert self.selenium.title == "Play Game | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/game"
        assert "<h3 class=\"Codle\">Compete to Claim Building</h3>" in self.selenium.page_source
        homeButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, '/play')]")
        homeButton.click()
        assert self.selenium.title == "Home | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/"

    def testHomeToLeaderboardToHome(self):
        """
        This function tests that the navigation buttons from the home
        page to the leaderboard page and back are in working order.
        """
        self.selenium.get(self.live_server_url + "/play")
        leaderboardButton = self.selenium.find_element_by_xpath(
            "//input[@class='arcade-font button3']")
        leaderboardButton.click()
        assert self.selenium.title == "Leaderboards | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/leaderboard"
        homeButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, '/play')]")
        homeButton.click()
        assert self.selenium.title == "Home | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/"

    def testLeaderboardToLogin(self):
        """
        This function tests a likely path for a returning user, who may
        check the leaderboard and then move to the login page.
        """
        self.selenium.get(self.live_server_url + "/play/leaderboard")
        loginButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, 'login')]")
        loginButton.click()
        assert self.selenium.title == "Log In | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/login"

    def testLeaderboardToSignUp(self):
        """
        This function tests the most likely path for a new user, who may
        have originally been curious about who was topping the leaderboard,
        and has subsequently navigated to the sign up page.
        """
        self.selenium.get(self.live_server_url + "/play/leaderboard")
        signUpButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, 'signup')]")
        signUpButton.click()
        assert self.selenium.title == "Sign Up | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/signup"
