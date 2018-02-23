
class MainPage(object):

    def __init__(self, browser):
        self.base_url ="https://flo-staging-pr-6228.herokuapp.com"
        self.browser = browser
        self.timeout = 30
        self.id_password = "id_password"
        self.preview_btn = '//*[@id="lockdown"]/form/p[2]/input'
        self.login_link = '//*[@id="app-root"]/div[3]/nav/div/div[3]/div/a[2]'
        self.logged_user = '.nav-user-name > a:nth-child(1)'
        self.request_quote = 'a.pricing__cta:nth-child(6)'
        self.quote_msg = '.heading--smallish'
        self.quote_download_btn = '#view_quote'
