<<<<<<< HEAD
# -*- coding:utf-8 -*-  
  
import re  
import urllib2  
import mechanize  
  
TARGET_URL = "http://ctf.idf.cn/game/pro/37/"  
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36 QQBrowser/3.5.3420.400"  
  
# Get target text use regular expression.  
def get_text(content):  
    return re.findall(r'<hr />(.*)<hr />', content,re.S)[0]  
  
def submit():  
  
    char_count = [0, 0, 0, 0, 0]  
  
    br_controller = mechanize.Browser()  
  
    br_controller.set_handle_equiv(True)  
    br_controller.set_handle_redirect(True)  
    br_controller.set_handle_referer(True)  
    br_controller.set_handle_robots(False)  
  
    br_controller.addheaders = [("User-Agent", USER_AGENT)]  
  
    br_controller.open(TARGET_URL)  
  
    # Get web page cotent  
    page_content = br_controller.response().read()  
  
    # Get target text  
    check_text = get_text(page_content)  
  
    # Calculate  
    for txt in check_text:  
        if txt == 'w':  
            char_count[0] += 1  
        elif txt == 'o':  
            char_count[1] += 1  
        elif txt == 'l':  
            char_count[2] += 1  
        elif txt == 'd':  
            char_count[3] += 1  
        elif txt == 'y':  
            char_count[4] += 1  
  
  
    # Change value in char_count to string.  
    result = ""  
    for nIndex in char_count:  
        result += str(nIndex)  
  
    print "Result = ", result  
  
    # Post form.  
    br_controller.select_form(nr=0)  
    br_controller.form['anwser'] = result  
    br_controller.submit()  
  
    print br_controller.response().read()  
  
if __name__ == '__main__':  
=======
# -*- coding:utf-8 -*-  
  
import re  
import urllib2  
import mechanize  
  
TARGET_URL = "http://ctf.idf.cn/game/pro/37/"  
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36 QQBrowser/3.5.3420.400"  
  
# Get target text use regular expression.  
def get_text(content):  
    return re.findall(r'<hr />(.*)<hr />', content,re.S)[0]  
  
def submit():  
  
    char_count = [0, 0, 0, 0, 0]  
  
    br_controller = mechanize.Browser()  
  
    br_controller.set_handle_equiv(True)  
    br_controller.set_handle_redirect(True)  
    br_controller.set_handle_referer(True)  
    br_controller.set_handle_robots(False)  
  
    br_controller.addheaders = [("User-Agent", USER_AGENT)]  
  
    br_controller.open(TARGET_URL)  
  
    # Get web page cotent  
    page_content = br_controller.response().read()  
  
    # Get target text  
    check_text = get_text(page_content)  
  
    # Calculate  
    for txt in check_text:  
        if txt == 'w':  
            char_count[0] += 1  
        elif txt == 'o':  
            char_count[1] += 1  
        elif txt == 'l':  
            char_count[2] += 1  
        elif txt == 'd':  
            char_count[3] += 1  
        elif txt == 'y':  
            char_count[4] += 1  
  
  
    # Change value in char_count to string.  
    result = ""  
    for nIndex in char_count:  
        result += str(nIndex)  
  
    print "Result = ", result  
  
    # Post form.  
    br_controller.select_form(nr=0)  
    br_controller.form['anwser'] = result  
    br_controller.submit()  
  
    print br_controller.response().read()  
  
if __name__ == '__main__':  
>>>>>>> 0b9dbfb320a073901bf33fe49fb8fcc85520109c
    submit() 