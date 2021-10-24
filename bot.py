from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    
    
    @staticmethod
    def simulando_digitacao(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            sleep(random.randint(1, 5)/30)

    
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        sleep(2)
        campo_usu = driver.find_element_by_xpath("//input[@name='username']")
        campo_usu.clear()
        campo_usu.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        sleep(5)
        self.comentar('programação')
    
    
    def comentar(self, hashtag):
        driver = self.driver
        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}')
        sleep(7)

        for i in range(1, 3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(2)
        
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]

        for pic_href in pic_hrefs:
            comentarios = ['Eu sou um bot', 'Estou em fase de teste', 'Fui criado por um programador', 'Eu sou feito em Python', 'Programação é vida!']
            driver.get(pic_href)
            sleep(3)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    
            
            try:
                driver.find_element_by_class_name("Ypffh")
                campo_comentario = driver.find_element_by_class_name("Ypffh").click()
                sleep(2, 5)
                self.simulando_digitacao(random.choise(comentarios), campo_comentario)
                sleep(random.randint(30, 45))
                driver.find_element_by_xpath('//button[contains(text(),"Publicar")]').click()
                sleep(7)
            except Exception as e:
                print(e)
                sleep(7)
          




        


