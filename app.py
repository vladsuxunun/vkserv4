from flask import Flask, url_for
import vk_api
import requests
import time
import random 
import os
from flask import render_template
app = Flask(__name__)


@app.route('/repost/<tokens>')
def hello(tokens):
  vk_session = vk_api.VkApi(token = tokens)
  time.sleep(3)
  vk = vk_session.get_api()
  vk1 = vk.newsfeed.getRecommended(count = 10)
  t1 = vk1['items']
  vv1 = vk1['items'][4]['source_id']
  vv2 = vk1['items'][4]['post_id']
  time.sleep(4)

  vk.wall.repost(object = ('wall' + str(vv1) + '_' + str(vv2)))
  time.sleep(15)
  vv1 = vk1['items'][8]['source_id']
  vv2 = vk1['items'][8]['post_id']
  vk.wall.repost(object = ('wall' + str(vv1) + '_' + str(vv2)))
  return 'Hello World'


@app.route("/about/<tokens>")
def about(tokens):
        vk_session = vk_api.VkApi(token = tokens)
        time.sleep(1)
        sex = 1
        path = ''
        #return(render_template('home.html', name=345))
        vk = vk_session.get_api()
        #vk.wall.post(message='Hello world!')
        time.sleep(1)
        sexi = vk.account.getProfileInfo()
        sex = sexi['sex']
        time.sleep(1)
        basedir = os.path.abspath(os.path.dirname(__file__))
        data_file = os.path.join(basedir, 'femalestatus.txt')
        data_file1 = os.path.join(basedir, 'fsurname.txt')
        with open(data_file1, encoding='utf-8') as f:
                surnames = f.read().splitlines()
                
        names = ['Маша','Мария','Валерия','Настя','Виктория','Яна','Ксения','Алиса','Альбина']
        if sex == 2:
            with open(data_file,encoding='utf-8') as f:
                status1 = f.read().splitlines()
            time.sleep(2)
            tex = status1[random.randint(0,28)]
            vk.account.saveProfileInfo(first_name = names[random.randint(0,8)],last_name =surnames[random.randint(0,65)],sex = 1,relation = 6,status = tex)
        elif sex == 1:
                with open(data_file,encoding='utf-8') as f:
                  status1 = f.read().splitlines()
                time.sleep(1)
                tex = status1[random.randint(0,28)]
                vk.account.saveProfileInfo(first_name = names[random.randint(0,8)],last_name =surnames[random.randint(0,65)],relation = 6,status = tex)
        elif sex == 0:
                with open(data_file,encoding='utf-8') as f:
                  status1 = f.read().splitlines()
                time.sleep(1)
                tex = status1[random.randint(0,28)]
                vk.account.saveProfileInfo(first_name = names[random.randint(0,8)],last_name =surnames[random.randint(0,65)],sex = 1,relation = 6,status = tex)
        time.sleep(1)
        path ='ss'+ str(random.randint(1,10))
        data_file = os.path.join(basedir, (path+'/' + str(random.randint(3,7))+ '.jpg'))
        upload = vk_api.VkUpload(vk_session)
       # photo = upload.photo_profile(path+'/' + str(random.randint(3,7))+ '.jpg')
        photo = upload.photo_profile(photo = data_file)
        album = vk.photos.createAlbum(title = 'фото')
        ss = album['id']
        for i in range(1,6):
            time.sleep(3)
            upload = vk_api.VkUpload(vk_session)
            data_file = os.path.join(basedir, (path +'/' + str(i) + '.jpg'))
            pr = upload.photo(photos=data_file,album_id =ss)
        return(render_template('home.html', name=345))
        
            


            #vk.messages.send(user_id ='204747021',message = 'владик'
            
    
            

           
            



if  __name__ == "__main__": 
    app.run(threaded=True, port=5000)