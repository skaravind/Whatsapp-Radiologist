from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pyautogui
from loreal import caption
import os
from chexnet import predict



def radio(images,action):
	image = images[-1]
	text_box = browser.find_element_by_class_name("_3u328")
	response = "Diagnosing... Please wait "+name+".\n"
	text_box.send_keys(response)
	action = webdriver.common.action_chains.ActionChains(browser)
	print('New image found, saving')
	sleep(5)
	save(image,action)
	try:
		preds = predict(path)
		c = 1
		text_box.send_keys('Top 3 probabilities :\n')
		for pred in preds:
			text_box.send_keys(str(c)+'. '+pred+'\n')#+' with probability:'+pred[1]+'\n')
			c += 1
	except Exception as e:
		print(e)
		text_box.send_keys('The image you sent is either too hard for me to understand or it is a server issue, you can try sending me image again\n')
	os.remove(path) # Cleanup


options = Options()
# options.set_headless(headless=True)
dirpath = os.getcwd()
browser = webdriver.Chrome(executable_path = dirpath+"/chromedriver")#firefox_options=options)
url = "https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en"
root = "https://news.google.com"
browser.get('https://web.whatsapp.com')
print('Scan and get started')
sleep(10)

path = '/Users/Karan/Downloads/WhatsappTest.jpg' #Your Downloads Path Here (Keep WhatsappTest.jpg as it is)


def save(image,action):
	'''To save the image'''
	action.context_click(image).perform()
	pyautogui.typewrite(['down','down','enter'])
	sleep(1.5)
	file = 'WhatsappTest.jpg'
	pyautogui.typewrite(file)
	sleep(0.5)
	pyautogui.typewrite(['enter'])
	sleep(3)



def getCaption(images,action):
	image = images[-1]
	text_box = browser.find_element_by_class_name("_3u328")
	response = "Analyzing... Please wait "+name+".\n"
	text_box.send_keys(response)
	action = webdriver.common.action_chains.ActionChains(browser)
	print('New image found, saving')
	sleep(4)
	save(image,action)
	try:
		cap = caption(path)
		text_box.send_keys('Prediction : "'+cap.capitalize()+'"\n')
	except Exception as e:
		print(e)
		text_box.send_keys('The image you sent is either too hard for me to understand or it is a server issue, you can try sending me image again\n')
	os.remove(path) # Cleanup


def getNews():
	text_box = browser.find_element_by_class_name("_3u328")
	response = "Let me fetch and send top 5 latest news:\n"
	text_box.send_keys(response)
	soup = BeautifulSoup(requests.get(url).content, "html5lib")
	articles = soup.find_all('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d YKEnGe EyNMab t6ttFe Fm1jeb EjqUne")
	news = [i.find_all('a',class_="ipQwMb Q7tWef")[0].text for i in articles[:5]]
	links = [root+i.find('a')['href'][1:] for i in articles[:5]]
	links = [requests.get("http://thelink.la/api-shorten.php?url="+link).content.decode() for link in links]
	for i in range(5):
		text_box.send_keys(news[i] + "==>" + links[i] + "\n")


bot_users = {}


while True:
	unread = browser.find_elements_by_class_name("P6z4j")
	if len(unread) > 0:
		ele = unread[0]
		action = webdriver.common.action_chains.ActionChains(browser)
		action.move_to_element_with_offset(ele, 0, -20)
		action.click()
		action.perform()
		sleep(2)
		name = browser.find_element_by_class_name("_1lpto").text
		print(name)
		message = browser.find_elements_by_class_name("FTBzM")[-1]
		images = message.find_elements_by_class_name("_18vxA")
		if 'activate bot' in message.text.lower():
			if name not in bot_users:
				bot_users[name] = True
				text_box = browser.find_element_by_class_name("_3u328")
				response = "Hi "+name+". Aravind's Bot here :). Now I am activated for you\n"
				text_box.send_keys(response)
		if name in bot_users:
			if len(images) != 0:
				# replace with radio
				getCaption(images, action)
			elif 'show' in message.text.lower() and 'news' in message.text.lower() and 'don' not in message.text.lower():
				getNews()
		if 'deactivate' in message.text.lower():
			if name in bot_users:
				text_box = browser.find_element_by_class_name("_3u328")
				response = "Bye "+name+".\n"
				text_box.send_keys(response)
				del bot_users[name]
	sleep(2)