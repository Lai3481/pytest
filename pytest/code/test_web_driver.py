from time import sleep

def test_youtube(dr_fix,search_fix,keys_fix):
    dr_fix.get('https://www.youtube.com/')

    sleep(2)

    all_win = dr_fix.window_handles
    print(all_win)


    sleep(1)

    dr_fix.find_element(search_fix.XPATH,'//*[@name="search_query"]').send_keys('jaychou')
    dr_fix.find_element(search_fix.XPATH,'//*[@name="search_query"]').send_keys(keys_fix.ENTER)
    # driver.find_element(By.XPATH,'//*[@id="search-icon-legacy"]/yt-icon/yt-icon-shape/icon-shape/div').click()

    sleep(1)

    all_win = dr_fix.window_handles
    print(all_win)
    dr_fix.switch_to.window(all_win[0])

    sleep(5)