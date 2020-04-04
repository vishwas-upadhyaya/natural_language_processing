from selenium import webdriver
import time
import csv

month=['1','2','3','4','5','6','7','8','9','10','11','12']
years=[2010,2011]
#dates=['Jan2' 'Jan3' 'Jan4' 'Jan5' 'Jan6' 'Jan7' 'Jan8' 'Jan9' 'Jan10' Jan11 Jan12 Jan13 Jan14 Jan15 Jan16 Jan17 Jan18 Jan19 Jan20 Jan21 Jan22 Jan23 Jan24 Jan25 Jan26 Jan27 Jan28 Jan29 Jan30 Jan31 Jan]
#day_in_month={'Jan':'31','Feb':'28','Mar':'31','Apr':'30','May':'31','Jun':'30','Jul':'31','Aug':'31','Sep':'30','Oct':'31','Nov':'30','Dec':'31'}
chromedriver='F:\download\chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver=webdriver.Chrome(chromedriver,options=options)
#driver.get("https://www.timeanddate.com/weather/india/new-delhi/historic?month=1&year=2010")
def get_numbers(text):
    a=''
    for i in list(text):
        #print(i)
        if str(i) in ['1','2','3','4','5','6','7','8','9','0']:
            a+=i
            #print(i)
    return a
#dr=driver.find_element_by_link_text("2 Jan").click()
#dr.send_keys()
#time.sleep(1)
#drt=driver.find_elements_by_xpath('/html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr')
#a=dr.click()
#print(len(drt))
#len_of_tr=len(drt)
all_data=[]
for year in years:



        for mon in month:
            try:
                driver.get("https://www.timeanddate.com/weather/india/new-delhi/historic?month=" + mon + "&year=" + str(year))
            except:
                time.sleep(10)
                driver.get("https://www.timeanddate.com/weather/india/new-delhi/historic?month=" + mon + "&year=" + str(year))

            try:
                day_length = driver.find_elements_by_xpath('/html/body/div[1]/div[7]/article/section[1]/div[5]/div[3]/a')
            except:
                time.sleep(10)
                day_length = driver.find_elements_by_xpath('/html/body/div[1]/div[7]/article/section[1]/div[5]/div[3]/a')
            day_len=[]
            for i in day_length:
                day_len.append(i.text)
            print(day_len)

            for day in day_len:
                temp = []
                wind=[]
                humidity = []
                press = []
                visibility = []
                try:
                    dr = driver.find_element_by_link_text(day).click()
                except:
                    time.sleep(10)
                    dr = driver.find_element_by_link_text(day).click()
                time.sleep(2)
                try:
                    drt = driver.find_elements_by_xpath('/html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr')
                except:
                    time.sleep(10)
                    drt = driver.find_elements_by_xpath('/html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr')
                len_of_tr = len(drt)
                for length in range(1,int(len_of_tr)+1):
                    for row_no in ['2','4','6','7','8']:
                        try:
                            data = driver.find_element_by_xpath('/html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr['+ str(length) +']/td['+ row_no +']')
                        except:
                            time.sleep(10)
                            try:
                                data = driver.find_element_by_xpath('/html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[' + str(length) + ']/td[' + row_no + ']')
                            except:
                                time.sleep(1)
                                data = driver.find_element_by_xpath('/html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[' + str(length) + ']/td[' + row_no + ']')
                        if row_no=='2':
                            if get_numbers(str(data.text))!='':
                                temp.append(int(get_numbers(str(data.text))))
                            else:
                                temp.append(0)
                        if row_no=='4':
                            if get_numbers(str(data.text))!='':
                                wind.append(int(get_numbers(str(data.text))))
                            else:
                                wind.append(0)
                        if row_no=='6':
                            if get_numbers(str(data.text)) != '':
                                humidity.append(int(get_numbers(str(data.text))))
                            else:
                                humidity.append(0)
                        if row_no=='7':
                            if get_numbers(str(data.text)) != '':
                                press.append(int(get_numbers(str(data.text))))
                            else:
                                press.append(0)
                        if row_no=='8':
                            if get_numbers(str(data.text)) != '':
                                visibility.append(int(get_numbers(str(data.text))))
                            else:
                                visibility.append(0)
                print(temp,wind,humidity,press,visibility)
                real_data=[round(sum(temp) / len(temp),2),round(sum(wind) / len(wind),2), round(sum(humidity) / len(humidity),2), round(sum(press) / len(press),2),round(sum(visibility) / len(visibility),2)]
                all_data.append([round(sum(temp) / len(temp),2), round(sum(humidity) / len(humidity),2), round(sum(press) / len(press),2),round(sum(visibility) / len(visibility),2)])
                print(all_data)
                with open('weather_data1.csv', 'a',newline='') as f:
                    s = csv.writer(f)
                    s.writerow([m for m in real_data])




# for i in dr:
#      print(i)
#      i.click()
#//*[@id="wt-his"]/tbody/tr[1]/td[2]
#/html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[1]/td[2]
#dr.find_element_by_xpath("//a[@href='javascript:showContent()']").click()

# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody
#
#/html/body/div[1]/div[7]/article/section[1]/div[5]/div[3]/a[1]
#
#/html/body/div[1]/div[7]/article/section[1]/div[5]/div[3]/a[1]


#/html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[2]/td[2]


#
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[1]/td[2]
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[1]/td[4]
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[1]/td[6]
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[1]/td[7]
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[1]/td[8]
#
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[2]/td[2]
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[2]/td[4]
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[2]/td[6]
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[2]/td[7]
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[2]/td[8]
#
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[3]/td[2]
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[3]/td[4]
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[3]/td[6]
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[3]/td[7]
# /html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[3]/td[8]


#/html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[8]/td[2]
#/html/body/div[1]/div[7]/article/section[1]/div[5]/div[2]/div/table/tbody/tr[8]/td[2]