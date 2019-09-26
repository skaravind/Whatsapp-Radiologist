# Whatsapp-Radiologist
A chatbot built in python using Selenium module that can predict lung diseases through Xray. I'm using the ChexNet's amazing model to accomplish this task accurately.

## Running the bot
1. If you want to test the image captioning bot feature, make sure you have put the Azure API key in loreal.py to use the image captioning bot feature.
2. Run the command <code>python3 bot.py</code>
3. Scan the QR code with your phone to start whatsapp web on browser that pops up. (You may have to configure selenium geckodriver depending on the OS you are using. Specify geckodriver.exe's path in selenium inside bot.py file)
4. Ask your friend to send <b>activate bot</b> to you.
5. Now he can either send <b>show news</b> or send an Xray to start the diagnosis.

Feel free to improve the code and add features.


Currently the chatbot is only capable of the following tasks:


## 1. Lung Xray Diagnosis
Using chexnet model. refer: https://github.com/brucechou1983/CheXNet-Keras for keras chexnet

and https://arxiv.org/pdf/1711.05225.pdf for the original paper.


## 2. Image Captioning Bot
A bot that captions the image sent to you using Microsoft's Azure platform. You will need an API key from Azure to run this. If you dont have one, you can make your own "caption" function and play around the image.

## 3.. News show
Any message you will get after you run the bot having the word "show news" in it will be treated as a request for latest headlines. The bot then fetches the latest news. 
