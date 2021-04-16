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

@app.route('/qiwi/<amount>/<comment>/<tel>')
def hellos(amount,comment,tel):
  s = requests.Session()
  s.headers = {'content-type':'application/json'}
  s.headers['authorization'] = 'Bearer ' + 'ab7eb95f66f6f5938fd1006751696a07'
  s.headers['User-Agent'] = 'Android v3.2.0 MKT'
  s.headers['Accept'] = 'application/json'
  postjson = {"id":"","sum":{"amount":"","currency":""},"paymentMethod":{"type":"Account","accountId":"643"}, "comment":"'+comment+'","fields":{"account":""}}
  postjson['id'] = str(int(time.time() * 1000))
  postjson['sum']['amount'] = amount
  postjson['sum']['currency'] = '643'
  postjson['fields']['account'] = tel
  postjson['comment'] = comment
  res = s.post('https://edge.qiwi.com/sinap/api/v2/terms/99/payments',json = postjson)
  return(render_template('home.html', name=345))




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
              
        names = ['Маша','Мария','Валерия','Настя','Виктория','Яна','Ксения','Алиса','Альбина','Алина','Вероника','Жанна','Полина','Ольга','Светлана','Валентина','Владислава','Василиса','Галина','Дарья','Дана','Ева','Лиза','Зоя','Инесса','Инга','Лариса','Лора','Надя','Оксана','Рита','Cоня','Элла','Фаина']
        if sex == 2:
            with open(data_file,encoding='utf-8') as f:
                status1 = f.read().splitlines()
            time.sleep(2)
            tex = status1[random.randint(0,28)]
            vk.account.saveProfileInfo(first_name = names[random.randint(0,33)],last_name =surnames[random.randint(0,65)],sex = 1,relation = 6,status = tex)
        elif sex == 1:
                with open(data_file,encoding='utf-8') as f:
                  status1 = f.read().splitlines()
                time.sleep(1)
                tex = status1[random.randint(0,28)]
                vk.account.saveProfileInfo(first_name = names[random.randint(0,33)],last_name =surnames[random.randint(0,65)],relation = 6,status = tex)
        elif sex == 0:
                with open(data_file,encoding='utf-8') as f:
                  status1 = f.read().splitlines()
                time.sleep(1)
                tex = status1[random.randint(0,28)]
                vk.account.saveProfileInfo(first_name = names[random.randint(0,33)],last_name =surnames[random.randint(0,65)],sex = 1,relation = 6,status = tex)
        time.sleep(1)
        path ='ss'+ str(random.randint(1,20))
        data_file = os.path.join(basedir, (path+'/' + str(random.randint(3,6))+ '.jpg'))
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
@app.route("/about1/<tokens>/<old_pass>")
def about1(tokens,old_pass):
        vk_session = vk_api.VkApi(token = tokens)
        time.sleep(1)
        sex = 1
        newpasswd = ('D' + old_pass + '1')
        path = ''
        #return(render_template('home.html', name=345))
        vk = vk_session.get_api()
        #vk.wall.post(message='Hello world!')
        #time.sleep(1)
        #sexi = vk.account.getProfileInfo()
        time.sleep(1)
        basedir = os.path.abspath(os.path.dirname(__file__))
        data_file = os.path.join(basedir, 'femalestatus.txt')
        data_file1 = os.path.join(basedir, 'fsurname.txt')
        with open(data_file1, encoding='utf-8') as f:
                surnames = f.read().splitlines()
                
        names = ['Маша','Мария','Валерия','Настя','Виктория','Яна','Ксения','Алиса','Альбина','Алина','Вероника','Жанна','Полина','Ольга','Светлана','Валентина','Владислава','Василиса','Галина','Дарья','Дана','Ева','Лиза','Зоя','Инесса','Инга','Лариса','Лора','Надя','Оксана','Рита','Cоня','Элла','Фаина']
        if sex == 2:
            with open(data_file,encoding='utf-8') as f:
                status1 = f.read().splitlines()
            time.sleep(2)
            tex = status1[random.randint(0,28)]
            vk.account.saveProfileInfo(first_name = names[random.randint(0,33)],last_name =surnames[random.randint(0,65)],sex = 1,relation = 6,status = tex)
        elif sex == 1:
                with open(data_file,encoding='utf-8') as f:
                  status1 = f.read().splitlines()
                time.sleep(1)
                tex = status1[random.randint(0,28)]
                vk.account.saveProfileInfo(first_name = names[random.randint(0,33)],last_name =surnames[random.randint(0,65)],sex = 1,relation = 6,status = tex)
        elif sex == 0:
                with open(data_file,encoding='utf-8') as f:
                  status1 = f.read().splitlines()
                time.sleep(1)
                tex = status1[random.randint(0,28)]
                vk.account.saveProfileInfo(first_name = names[random.randint(0,33)],last_name =surnames[random.randint(0,65)],sex = 1,relation = 6,status = tex)
        time.sleep(1)
        path ='ss'+ str(random.randint(1,20))
        random_avatar = random.randint(1,3)
        data_file = os.path.join(basedir, (path+'/' + str(random_avatar)+ '.jpg'))
        upload = vk_api.VkUpload(vk_session)
       # photo = upload.photo_profile(path+'/' + str(random.randint(3,7))+ '.jpg')
        photo = upload.photo_profile(photo = data_file)
        album = vk.photos.createAlbum(title = 'фото')
        ss = album['id']
        for i in range(1,6):
          if random_avatar == i:
            pass
          else:
            time.sleep(3)
            upload = vk_api.VkUpload(vk_session)
            data_file = os.path.join(basedir, (path +'/' + str(i) + '.jpg'))
            pr = upload.photo(photos=data_file,album_id =ss)
        
        account_success ="--"

        try:
            ss = vk.account.changePassword(old_password=old_pass,new_password=newpasswd)
            tokz = ss['token']
            account_success = "+"
        except:
            newpasswd = passwd
            tokz = tokens
            account_success = "-"
        return(newpasswd+ ":" + tokz + ":" + account_success)  



@app.route("/about3/<tokens>/<old_pass>")
def about3(tokens,old_pass):
        success_auth = 0
        success_photo = 0
        account_success ="-"
        sex = 1
        old_pass = old_pass[1:(len(old_pass) - 1)]
        newpasswd = ('D' + old_pass + '1')
        path = ''
        #vk.wall.post(message='Hello world!')
        #time.sleep(1)
        #sexi = vk.account.getProfileInfo()
        basedir = os.path.abspath(os.path.dirname(__file__))
        data_file = os.path.join(basedir, 'malestatus.txt')
        data_file1 = os.path.join(basedir, 'msurname.txt')
        vk_session = vk_api.VkApi(token = tokens)
        time.sleep(1)
        vk = vk_session.get_api()
        with open(data_file1, encoding='utf-8') as f:
            surnames = f.read().splitlines()
        with open(data_file, encoding='utf-8') as f:
              status1 = f.read().splitlines()
        names = ['Александр','Сергей','Анатолий','Даниил','Илья','Никита','Владислав','Станислав','Слава']
        try:
            if sex == 2:
                  time.sleep(1)
                  tex = status1[random.randint(0,26)]
                  vk.account.saveProfileInfo(first_name = names[random.randint(1,30)],last_name =surnames[random.randint(1,62)],sex = 1,relation = 6,status = tex)
            elif sex == 1:
                  time.sleep(1)
                  tex = status1[random.randint(1,22)]
                  vk.account.saveProfileInfo(first_name = names[random.randint(1,7)],last_name =surnames[random.randint(1,6)],sex = 2,status = tex)    
            elif sex == 0:
                 time.sleep(1)
                 tex = status1[random.randint(0,26)]
                 vk.account.saveProfileInfo(first_name = names[random.randint(1,30)],last_name =surnames[random.randint(1,62)],sex = 1,relation = 6,status = tex)
                 time.sleep(2)
            success_auth = 1
        except:
            pass

        if success_auth == 1:
            try:
                path ='ss'+ str(random.randint(100,103))
                random_avatar = random.randint(1,3)
                data_file = os.path.join(basedir, (path+'/' + str(random_avatar)+ '.jpg'))
                upload = vk_api.VkUpload(vk_session)

                photo = upload.photo_profile(photo = data_file)
                album = vk.photos.createAlbum(title = 'фото')
                ss = album['id']
                for i in range(1,6):
                   if random_avatar == i:
                       pass
                   else:
                       time.sleep(2)
                       upload = vk_api.VkUpload(vk_session)
                       data_file = os.path.join(basedir, (path +'/' + str(i) + '.jpg'))
                       pr = upload.photo(photos=data_file,album_id =ss)
                success_photo = 1
            except:
                pass

        if success_auth == 1:
            try:
                ss = vk.account.changePassword(old_password=old_pass,new_password=newpasswd)
                tokz = ss['token']
                account_success = "+"
            except:
                newpasswd = old_pass
                tokz = tokens
                account_success = "-"
        else:
             newpasswd = old_pass
             tokz = tokens
             account_success = "-"
        return(newpasswd+ ":" + tokz + ":" + account_success +  ":" + str(success_auth)+  ":" + str(success_photo) )  


@app.route("/about2/<tokens>/<old_pass>")
def about2(tokens,old_pass):
        success_auth = 0
        success_photo = 0
        account_success ="-"
        sex = 1
        old_pass = old_pass[1:(len(old_pass) - 1)]
        newpasswd = ('D' + old_pass + '1')
        path = ''
        #vk.wall.post(message='Hello world!')
        #time.sleep(1)
        #sexi = vk.account.getProfileInfo()
        basedir = os.path.abspath(os.path.dirname(__file__))
        data_file = os.path.join(basedir, 'femalestatus.txt')
        data_file1 = os.path.join(basedir, 'fsurname.txt')
        vk_session = vk_api.VkApi(token = tokens)
        time.sleep(1)
        vk = vk_session.get_api()
        with open(data_file1, encoding='utf-8') as f:
            surnames = f.read().splitlines()
        with open(data_file, encoding='utf-8') as f:
              status1 = f.read().splitlines()
        names = ['Маша','Мария','Валерия','Настя','Виктория','Яна','Ксения','Алиса','Альбина','Алина','Вероника','Жанна','Полина','Ольга','Светлана','Валентина','Владислава','Василиса','Галина','Дарья','Дана','Ева','Лиза','Зоя','Инесса','Инга','Лариса','Лора','Надя','Оксана','Рита','Cоня','Элла','Фаина']
        try:
            if sex == 2:
                  time.sleep(1)
                  tex = status1[random.randint(0,26)]
                  vk.account.saveProfileInfo(first_name = names[random.randint(1,30)],last_name =surnames[random.randint(1,62)],sex = 1,relation = 6,status = tex)
            elif sex == 1:
                  time.sleep(1)
                  tex = status1[random.randint(1,26)]
                  vk.account.saveProfileInfo(first_name = names[random.randint(1,30)],last_name =surnames[random.randint(1,62)],sex = 1,relation = 6,status = tex)    
            elif sex == 0:
                 time.sleep(1)
                 tex = status1[random.randint(0,26)]
                 vk.account.saveProfileInfo(first_name = names[random.randint(1,30)],last_name =surnames[random.randint(1,62)],sex = 1,relation = 6,status = tex)
                 time.sleep(2)
            success_auth = 1
        except:
            pass

        if success_auth == 1:
            try:
                path ='ss'+ str(random.randint(1,20))
                random_avatar = random.randint(1,3)
                data_file = os.path.join(basedir, (path+'/' + str(random_avatar)+ '.jpg'))
                upload = vk_api.VkUpload(vk_session)

                photo = upload.photo_profile(photo = data_file)
                album = vk.photos.createAlbum(title = 'фото')
                ss = album['id']
                for i in range(1,6):
                   if random_avatar == i:
                       pass
                   else:
                       time.sleep(2)
                       upload = vk_api.VkUpload(vk_session)
                       data_file = os.path.join(basedir, (path +'/' + str(i) + '.jpg'))
                       pr = upload.photo(photos=data_file,album_id =ss)
                success_photo = 1
            except:
                pass

        if success_auth == 1:
            try:
                ss = vk.account.changePassword(old_password=old_pass,new_password=newpasswd)
                tokz = ss['token']
                account_success = "+"
            except:
                newpasswd = old_pass
                tokz = tokens
                account_success = "-"
        else:
             newpasswd = old_pass
             tokz = tokens
             account_success = "-"
        return(newpasswd+ ":" + tokz + ":" + account_success +  ":" + str(success_auth)+  ":" + str(success_photo) )  
           
            



if  __name__ == "__main__": 
    app.run(threaded=True, port=5000)