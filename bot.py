# -*- coding: utf-8 -*-
from linepy import *; import time, threading; ts = time.time();cl = LINE(""); cl.log(cl.authToken); AuthToken = []
from datetime import datetime
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import requests
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz,  urllib, urllib.parse,timeit,atexit,youtube_dl,pafy
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit,youtube_dl,pafy
from gtts import gTTS
from googletrans import Translator
from threading import Thread
#==============================================================================#
cl.log(cl.authToken)
AuthToken = []
#==============================================================================#
for i in range(1, 1): AuthToken.append(LINE(cl.authToken))
#==============================================================================#
botStart = time.time()
#==============================================================================#
#==============================================================================#
clMID = cl.profile.mid
profile = cl.getProfile()
status = str(profile.statusMessage)
lock = _name = ""
if lock not in status:
    profile.statusMessage = lock + status
    cl.updateProfile(profile)
else:
    pass
settings = {
    "changePicture": True
}
clProfile = cl.getProfile()
clMID = cl.profile.mid
#KAC = [cl]
#Bots = [clMID]

msg_dict = {}
msg_dictt = {}

clProfile = cl.getProfile()

Unlist = []

lineSettings = cl.getSettings()

oepoll = OEPoll(cl)
#==============================================================================#
####################################################
readOpen = codecs.open("read.json","r","utf-8")
read = json.load(readOpen)
####################################################
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)
####################################################
redOpen = codecs.open("red.json","r","utf-8")
red = json.load(redOpen)
####################################################
jgOpen = codecs.open("jg.json","r","utf-8")
jg = json.load(jgOpen)
####################################################
banOpen = codecs.open("ban.json","r","utf-8")
ban = json.load(banOpen)
####################################################

bl = [""]
msg_dict = {}
msg_dictt = {}
restart = True
wait = {
    'logout': {},
    'rapidFire': {},
    'group': "",
    'getmid': True,
    'Unlist': True,#序列收回
    'cvp': True,#更換頭貼
    'gbc':{},
    'resset': True#偵測更新
    }
####################################################
readOpen = codecs.open("read.json","r","utf-8")
read = json.load(readOpen)
####################################################
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)
####################################################
redOpen = codecs.open("red.json","r","utf-8")
red = json.load(redOpen)
####################################################
jgOpen = codecs.open("jg.json","r","utf-8")
jg = json.load(jgOpen)
####################################################
banOpen = codecs.open("ban.json","r","utf-8")
ban = json.load(banOpen)
####################################################    
datadir = {"switch": False,"gid": ""}    
#==============================================================================#
####################################################
mulai = time.time()
####################################################
def kick(n, to, mid):
    while 1: AuthToken[n].kickoutFromGroup(to, mid); break
def restartBot():
    print ("[D.H.Z公共主機_ŁÏŃĚ_ßöᴛ系統通知]機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#Youtube網址
def yturl(url):
    video = pafy.new(url)
    best = video.getbest() 
    return best.url
#Youtube下載
def ytdl(url):
    video = pafy.new(url)
    best = video.getbest() 
    best.download(filepath="test.mp4")
def ytdl(url):
    video = pafy.new(url)
    best = video.getbest() 
    best.download(filepath="test.mp4")    
def Runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 天\n%02d 小時\n%02d 分鐘\n%02d 秒\n運行時間\n半垢 運行時間' % (days, hours, mins, secs)
def Runtimeself(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d天%02d小時%02d分鐘%02d秒' % (days, hours, mins, secs)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = ban
        f = codecs.open('ban.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = jg
        f = codecs.open('jg.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def logError(text):
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invaliod mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
            textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def helpmessage():
    helpMessage = """—✪〘 D.H.Z公共主機指令分類 〙✪—
【dhz:Help】 查看指令面板
【Help1】 查看系統指令
【Help2】 查看機器設定
【Help3】 查看資料訊息
【Help4】 查看黑單功能
【Help5】 查看群組功能
【Help6】 查看輔助功能
【Help7】 查看踢人功能
【Help8】 查看特別功能
【Help9】 查看專武功能
【Help10】查看外接功能
【Help11】查看版本資訊
【Help12】查看刷人功能
【Help13】查看邀請功能
【Help14】查看換頭功能
—〘感謝使用D.H.Z公共主機〙—"""
    return helpMessage
def helpmessagenut():
    helpMessageNUT = """此機器指令面板非「help」\n請輸入「dhz:help」"""
    return helpMessageNUT    
def helpmessagebot():
    helpMessageBOT = """♨━狀態━♨
•Sp 速度
•sat 處理測試表
•speed 速度測試表
•Set 設定
•Mine 關於規制狀態
•About 關於自己
•.tn 多工線程報數    
•Me 我的連結
•MyMid 我的mid
•MyName 我的名字
•MyBio 個簽
•MyPicture 我的頭貼
•myvid 我的影片
•MyCover 我的封面
•Contact @ 標註取得連結
•Mid @ 標註查mid
•gc @ 簡單查看標註者資訊
•contact @ 查看標註者友資
•Name @ 完整查看標註者資訊"""
    return helpMessageBOT
def helpmessageset():
    helpMessageSET = """━♪設定♪━
•Add On/Off 自動加友
•Bl On/Off 自動封鎖
•Join On/Off 自動進群
•Leave On/Off 離開副本
•Read On/Off 自動已讀
•Share On/Off 權限公開
•Game On/Off 遊戲開啟/關閉
•sp On/Off 入群頭貼
•sl On/Off 入群通知
•sj On/Off 退群通知
•kc On/Off 踢人通知
•ReRead On/Off 查詢收回
•Pro On/Off 所有保護
•pr On/Off 踢人保護
•qr On/Off 網址保護
•ip On/Off 邀請保護
•jg On/Off 進群保護
•Getmid On/Off 取得MID
•Detect On/Off 標註偵測
•cvp on/off 換頭
•rg on/off 極速收回
•cp on/off 偵測更新帳號
•Timeline On/Off 文章網址 """
    return helpMessageSET
def helpmessageme():
    helpMessageME = """━♪查詢♪━
•youtube:(影片關鍵字) YT影片查詢
•google:(內容關鍵字)  GOOGLE文字查詢"""
    return helpMessageME
def helpmessageban():
    helpMessageBAN = """━♪權黑指令♪━
•addop @ 新增權限
•delop @ 刪除權限
•Ban @ 加入黑單
•Mb:mid 使用系統識別碼將該用戶加入黑單
•Mub:mid 使用系統識別碼將該用戶解除黑單
•Unban @ 取消黑單
•Nkban 踢除黑單
•CleanBan 清空黑單
•Oplist 查看權限表
•Banlist 查看黑單"""
    return helpMessageBAN
def helpmessagegrp():
    helpMessageGRP = """━♪群組♪━
•Group 創群者
•GroupId 群組ID
•GroupName 群組名稱
•GroupPicture 群組圖片
•GroupLink 群組網址
•Link On/Off 網址開/關
•update 網址更新
•Lg 所有群組列表
•Gb 成員名單
•Ginfo 群組資料
•Gn (文字) 更改群名
•Cancel 取消所有邀請
•Tg (群組mid) 遠程查看群組成員
•Te (群組mid) 遠程查看群組邀請成員"""
    return helpMessageGRP
def helpmessageatl():
    helpMessageATL = """━♪輔助♪━
•Tagall 標註全體
•Zc 發送0字元友資
•SR 已讀點設置
•DR 取消偵測
•LR 已讀偵測
•mall:次數 群組通話邀請
•rall:次數 副本通話邀請
•mc (MID) mid獲取友資"""
    return helpMessageATL
def helpmessagemin():
    helpMessageMIN = """━♪踢人♪━
•Nk @ 單、多踢
•Zk @ 單踢
•Nkban 踢除黑名單
•Zk 踢出0字元
•Ri @ 來回機票"""
    return helpMessageMIN
def helpmessageadd():
    helpMessageADD = """━♪特別功能♪━
•ii @ 次數  標註邀機
•mc:(MID) mid獲取友資
•Ni (名字) 邀請未定名好友
•Di (名字) 邀請已定名好友
•Tg:(群組mid) 遠程查看群組成員
•Te:(群組mid) 遠程查看群組邀請成員
•Tn*@* 更改定名
•Ac (名字) 使用名字丢出友資
•Ty 私聊強制標住
•us [次數] 極速收回訊息"""
    return helpMessageADD
def helpmessagegkb():
    helpMessageGKB = """━♪專武功能♪━
• kick on 專武開啟
• kick off 專武關閉
• .set 專武資料
• .sp 專武測速
• .ct 翻群
• .1 D.H.Z公共主機翻群
• .2 愛滋翻群
• .3 一般翻群
• .ttk @ 專武踢人
• nnk:(TEXT) 專武名字踢人
• .tta @ 加入專武踢人名單
• .ttd @ 刪除專武踢人名單
• .tna (名字) 加入專武踢人名單
• .tnd  (名字) 刪除專武踢人名單
• .tlist 查看專武踢人名單
• .ctlist 清空專武踢人名單
• .gogo 踢除專武名單者"""
    return helpMessageGKB
def helpmessageext():
    helpMessageEXT = """━♪外接指令♪━
•tr-Tw (text) 翻譯成中文
•tr-En (text) 翻譯日文
•tr-Jp (text) 翻譯英文
•tr-Id (text)  翻譯印尼文
•send-tw (text) 用中文說
•send-en (text) 用英文說
•send-jp (text) 用日文說
•send-id (trxt) 用印尼文說"""
    return helpMessageEXT
def helpmessagever():
    helpMessageVER = """━♪版本資訊♪━
•Rb 重新啟動
•Save 儲存設定
•Ren 運作時間
•bye 機器退出群組
•About 關於本帳
•Cn:(text) 更改名子
•Cb:(text) 更改個簽
•lg 查看自己在的群組
•logout 直接登出"""
    return helpMessageVER
def helpmessagetag():
    helpMessageTAG = """━♪刷人♪━
•Sy [內容 次數] 重複講話
•Rex [標人+內容 次數] 重複標人講話
•Tag @ [次數] 重複標人
•Ty 私聊強制標住
•Copy @ 複製標著者
•us [次數] 極速收回訊息"""
    return helpMessageTAG
def helpmessageinv():
    helpMessageINV = """━♪邀請♪━
•Ni: (名字) 邀請未定名好友
•Di: (名字) 邀請已定名好友    
•Botsadd @ 加入自動邀請
•Botsdel @ 取消自動邀請
•Botslist 自動邀請表
•Join 自動邀請
•ii @ 次數  標註邀機
•Inv (mid) 透過mid邀請
•Inv @ 標註多邀"""
    return helpMessageINV   
def helpmessagecvp():
    helpMessageCVP = """━♪換頭貼功能♪━
•cv:YT影片網址(影片✔圖片✔)
•ytmp3:YT影片網址(純音樂✔保留原有頭像✔)
•ytmp4:YT影片網址(純影片✔沒有原有頭像✔)"""
    return helpMessageCVP      
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
admin=['']
owners=['u3d07fc517427da2f8dff71630873ee4f','u5a934d08f5abccc26d6afed8d8dd1a06','u0b87b6b0730c8f48aa583dedb05e26a1','u9c0b65006e756c237622c54ad2d7f48f',clMID]
#if clMID not in owners:
#    python = sys.executable
#    os.execl(python, python, *sys.argv)
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "安安！{} 感謝您加我為好友！D.H.Z公共主機_βộṱ_V8.2.5 ŁÏŃĚ ßöᴛ 運行中(๑′ᴗ‵๑)！D.H.Z公共主機™™™™我的作者網址:line.me/ti/p/~lovewm1010".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 1:
            print ("[ 1 ] 個簽鎖定")
            if cl.getProfile().mid != admin:
                if op.param1 == "16":
                    _name = ""
                    _name += ""
                    _name += ""
                    _name += ""
                    _name += ""
                    _name += ""
                    _name += ""
                    contact = cl.getProfile()
                    status = contact.statusMessage
                    if _name not in  cl.getProfile().statusMessage:
                        profile = cl.getProfile()
                        profile.statusMessage =  _name + status
                        cl.updateProfile(profile)
        if op.type == 2:
            contact = cl.getContact(op.param1)
            if wait["resset"] == True:
                if op.param2 == "2":
                    cl.sendMessage(op.param1,"[自動發送]\n發現你改名稱摟!!!\n作者:D.H.Z公共主機\n作者網址:https://line.me/ti/p/~lovewm1010\n•此為自動偵測訊息☆")
                    cl.sendMessage("MID","通知好友更改名稱:\n" + contact.displayName)
                if op.param2 == "8":
                    cl.sendMessage(op.param1,"[自動發送]\n發現你更改頭貼/動態頭貼摟!!!\n作者:D.H.Z公共主機\n作者網址:https://line.me/ti/p/~lovewm1010\n•此為自動偵測訊息☆")
                    cl.sendMessage("MID","通知好友更改動態頭貼:\n" + contact.displayName)
                if op.param2 == "16":
                    cl.sendMessage(op.param1,"[自動發送]\n發現你更改個簽摟!!!\n作者:D.H.Z公共主機\n作者網址:https://line.me/ti/p/~lovewm1010\n•此為自動偵測訊息☆")
                    cl.sendMessage("MID","通知好友更改個簽:\n" + contact.displayName)
        if op.type == 5:#自動防封鎖
            print ("[ 5 ] INV PRO")
            if settings["invBlock"] == True:
                cl.blockContact(op.param1)
                cl.sendMessage(op.param1, "•防邀機功能運行中•\n•[已啟動自動封鎖]•\nÇręätør:D.H.Z公共主機 我的作者網址:line.me/ti/p/~lovewm1010".format(str(cl.getContact(op.param1).displayName)))            
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin or op.param2 in ban["bots"]:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)               
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            if clMID in op.param3:
                group = cl.getGroup(op.param1)
                if settings["autoJoin"] == True:                    
                       cl.acceptGroupInvitation(op.param1)
                       cl.sendMessage(op.param1,"☰☱☲☳自動入群☴☵☶☷\n•多工公開招待使用中.....\n•感謝您的邀請!!!\n•我的作者:line.me/ti/p/~lovewm1010\n☰☱☲☳結束☴☵☶☷")                
            else:
                group = cl.getGroup(op.param1)
                gInviMids = []
                for z in group.invitee:
                    if z.mid in ban["blacklist"]:
                        gInviMids.append(z.mid)
                if gInviMids == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, gInviMids)
                    cl.sendMessage(op.param1,"被邀請者在黑名單...")
        if op.type == 15:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeLeave"] == True:
                try:
                    arrData = ""
                    text = "%s "%('提示')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "退出了 {} 的大家庭！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)  
        if op.type == 60:
            if op.param1 in jg["JoinGroup"]:
                if op.param2 not in admin:
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except Exception as e:
                        print(e)                      
        if op.type == 17:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeJoin"] == True:
                try:
                    arrData = ""
                    text = "%s "%('歡迎')
                    arr = []
                    mention = "@x "
                    name = str(cl.getGroup(op.param1).name)
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + " 加入 {} 的大家庭!".format(str(group.name))           
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 25:
            msg = op.message           
            Unlist.append(msg.id)
               #極限收回
                            
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        try:
                            arrData = ""
                            text = "%s " %('警告')
                            arr = []
                            mention1 = "@arasi "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention1) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention1 + '踢了 '
                            mention2 = "@kick "
                            sslen = str(len(text))
                            eelen = str(len(text) + len(mention2) - 1)
                            arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                            arr.append(arrdata)
                            text += mention2
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            settings["blacklist"][op.param2] = True
                            cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
            else:
                if settings["kickContact"] == True:
                    try:
                        arrData = ""
                        text = "%s " %('警告')
                        arr = []
                        mention1 = "@arasi "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention1) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention1 + '踢了 '
                        mention2 = "@kick "
                        sslen = str(len(text))
                        eelen = str(len(text) + len(mention2) - 1)
                        arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                        arr.append(arrdata)
                        text += mention2
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
                else:
                     pass
        if op.type == 60:
            if op.param1 in jg["JoinGroup"]:
                if op.param2 not in admin:
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except Exception as e:
                        print(e)             
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25 or op.type == 26:
            K0 = admin
            msg = op.message
            if settings["share"] == True:
                K0 = msg._from
            else:
                K0 = admin
#        if op.type == 25 :
#            if msg.toType ==2:
#                g = cl.getGroup(op.message.to)
#                print ("sended:".format(str(g.name)) + str(msg.text))
#            else:
#                print ("sended:" + str(msg.text))
#        if op.type == 26:
#            msg =op.message
#            pop = cl.getContact(msg._from)
#            print ("replay:"+pop.displayName + ":" + str(msg.text))
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in sender:
                if text.lower() == '遊戲':        
                    if settings["newGame"] == True:
                        cl.sendReplyMessage(msg.id, to,"[遊戲內容]\n運勢\n猜拳\n音樂[=感謝使用=]")
            if sender in sender:
                if text.lower() == '運勢':        
                    if settings["newGame"] == True:
                        data = random.choice(['[運勢結果]\n撿到100元～有點手氣！','[運勢結果]\n撿到500元～運氣可以^_^','[運勢結果]\n撿到50元～有點不好...','[運勢結果]\n沒撿到～慘了慘了...','[運勢結果]\n撿到1000元～手氣旺旺！'])
                        cl.sendReplyMessage(msg.id, to,str(data))
            if sender in sender:
                if text.lower() == '音樂':        
                    if settings["newGame"] == True:
                        data = random.choice(['[推薦音樂]\nhttps://youtu.be/vWcVQZ-NQsg','[推薦音樂]\nhttps://youtu.be/a4eR-5OJ-7Q','[推薦音樂]\nhttps://youtu.be/b35Vwj0aFxY','[推薦音樂]\nhttps://youtu.be/ryP_nQYYaYY','[推薦音樂]\nhttps://youtu.be/Hl3L9_VK7wM','[推薦音樂]\nhttps://youtu.be/ATblV50Odx8','[推薦音樂]\nhttps://youtu.be/Kc5BCtfFzDg','[推薦音樂]\nhttps://youtu.be/TQ5w9KHHa9M','[推薦音樂]\nhttps://youtu.be/yjM25-Z38_4','[推薦音樂]\nhttps://youtu.be/wdH26D8Ssww','[推薦音樂]\nhttps://youtu.be/jfzOlIVBGzM','[推薦音樂]\nhttps://youtu.be/iIF2ikZfoxw','[推薦音樂]\nhttps://youtu.be/WmW9Fh4Msu4','[推薦音樂]\nhttps://youtu.be/kO77K3dEMpA','[推薦音樂]\nhttps://youtu.be/_9gvo2aClpk','[推薦音樂]\nhttps://youtu.be/aAkMkVFwAoo','[推薦音樂]\nhttps://youtu.be/VhHQyb4r9Xg','[推薦音樂]\nhttps://youtu.be/xrooMGuRhgY','[推薦音樂]\nhttps://youtu.be/ZeN007qFHFM'])
                        cl.sendReplyMessage(msg.id, to,str(data))
            if sender in sender:
                if text.lower() == '猜拳':
                    if settings["newGame"] == True:
                        cl.sendReplyMessage(msg.id, to, "[猜拳遊戲]\n輸入：\n剪刀，石頭，布\n\n來一決高下吧！")
            if sender in sender:
                if text.lower() == '剪刀':        
                    if settings["newGame"] == True:
                        data = random.choice(['[猜拳結果]\n你出剪刀✌\n我出石頭👊\n\n👻你輸了-垃圾！👻','[猜拳結果]\n你出剪刀✌\n我出布✋\n\n🎉你贏了-滾拉！🎉','[猜拳結果]\n你出剪刀✌\n我出剪刀✌\n\n👏平手-算你好運！👏'])
                        cl.sendReplyMessage(msg.id, to,str(data))
            if sender in sender:
                if text.lower() == '石頭':        
                    if settings["newGame"] == True:
                        data = random.choice(['[猜拳結果]\n你出石頭👊\n我出石頭👊\n\n👏平手！-想贏嗎?👏','[猜拳結果]\n你出石頭👊\n我出布✋\n\n👻你輸了！-笑死👻','[猜拳結果]\n你出石頭👊\n我出剪刀✌\n\n🎉你贏了！-阿不就很邱🎉'])
                        cl.sendReplyMessage(msg.id, to,str(data))  
            if sender in sender:
                if text.lower() == '布':        
                    if settings["newGame"] == True:
                        data = random.choice(['[猜拳結果]\n你出布✋\n我出石頭\n\n🎉你贏了！-剛好而已🎉','[猜拳結果]\n你出布✋\n我出布✋\n\n👏平手！-喔👏','[猜拳結果]\n你出布✋\n我出剪刀✌\n\n👻你輸了！-知道了嗎👻'])
                        cl.sendReplyMessage(msg.id, to,str(data))                
#==============================================================================#
            if sender in K0 or sender in owners:
               
                if text.lower() == 'help':
                    helpMessageNUT = helpmessagenut()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageNUT)) 
                if text.lower() == 'dhz:help':
                    helpMessage = helpmessage()
                    cl.sendReplyMessage(msg.id, to, str(helpMessage))       
                if text.lower() == 'help1':
                    helpMessageBOT = helpmessagebot()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageBOT))
                if text.lower() == 'help2':
                    helpMessageSET = helpmessageset()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageSET))
                if text.lower() == 'help3':
                    helpMessageME = helpmessageme()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageME))
                if text.lower() == 'help4':
                    helpMessageBAN = helpmessageban()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageBAN))
                if text.lower() == 'help5':
                    helpMessageGRP = helpmessagegrp()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageGRP))
                if text.lower() == 'help6':
                    helpMessageATL = helpmessageatl()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageATL))
                if text.lower() == 'help7':
                    helpMessageMIN = helpmessagemin()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageMIN))
                if text.lower() == 'help8':
                    helpMessageADD = helpmessageadd()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageADD))
                if text.lower() == 'help9':
                    helpMessageGKB = helpmessagegkb()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageGKB))
                if text.lower() == 'help10':
                    helpMessageEXT = helpmessageext()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageEXT))
                if text.lower() == 'help11':
                    helpMessageVER = helpmessagever()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageVER))     
                if text.lower() == 'help12':        
                    helpMessageTAG = helpmessagetag()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageTAG))
                if text.lower() == 'help13':        
                    helpMessageINV = helpmessageinv()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageINV))    
                if text.lower() == 'help14':        
                    helpMessageCVP = helpmessagecvp()
                    cl.sendReplyMessage(msg.id, to, str(helpMessageCVP))                
            
#==============================================================================#
                elif ".sp" == text.lower():
                    t1 = time.time()
                    threading.Thread(target=cl.sendReplyMessage, args=(msg.id, to, "•專武速度測試•",)).start()
                    t2 = time.time() - t1
                    time.sleep(0.1)
                    return cl.sendReplyMessage(msg.id, to, "•%s seconds•" %t2)
                elif text.lower() == 'speed':
                    ret_ = "［ 反應速度 ］"
                    ret_ += "\nThe First Term:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\nThe Second Term:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\nThe Third Term:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\nThe Fouth Term:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\nThe Firth Term:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\n［ 處理速度 ］"
                    ret_ += "\nThe First Term:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\nThe Second Term:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\nThe Third Term:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\nThe Fouth Term:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\nThe Firth Term:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\n［ That is the Test End ］"
                    cl.sendReplyMessage(msg.id, to, str(ret_))
                    cl.sendMessage("u3c3e610adde063db1eb442612c5d2f98", "表格速度檢查中......")
                elif text.lower() == 'sat':
                    ret_ = "［ 全部速度 ］"
                    ret_ += "\n回傳速度:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=1000))
                    ret_ += "\n群組邀請:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\n好友讀取:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=1000))
                    ret_ += "\n友資讀取:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=1000))
                    ret_ += "\n群組讀取:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\n［ 完 ］"
                    cl.sendReplyMessage(msg.id, to, str(ret_))  
                    cl.sendMessage("u3c3e610adde063db1eb442612c5d2f98", "各單位檢查中......")  
                elif text.lower() == 'sp':
                    cl.sendReplyMessage(msg.id, to,""+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100)) + " seconds")
                elif text.lower() == 'save':
                    backupData()
                    cl.sendReplyMessage(msg.id, to,"儲存設定成功!")
                elif text.lower() == 'rb':
                    cl.sendReplyMessage(msg.id, to, "重新啟動中...")
                    time.sleep(5)
                    cl.sendReplyMessage(msg.id, to, "重新啟動成功\n☰☱☲☳☰☱☲☳\n重新啟動版本《V8.2.5》")
                    restartBot()
                elif text.lower() == 'ren':
                    eltime = time.time() - mulai
                    bot = "運行時間長達\n" + Runtime(eltime)
                    cl.sendReplyMessage(msg.id, to,bot)    
                elif msg.text.startswith("us "):
                    num = msg.text.replace("us ","")
                    ber = 0
                    for x in reversed(Unlist):
                        cl.unsendMessage(x)
                        Unlist.remove(x)
                        ber += 1
                        if ber == int(num)+1:
                            break        
                elif msg.text == "Ty": 
                    cl.sendTag(msg.to, msg.to)
                elif msg.text == "ty": 
                    cl.sendTag(msg.to, msg.to)    
                elif msg.text.startswith("Ytmp3:"):
                    sep = msg.text.replace("Ytmp3:","")
                    search = msg.text.replace("Ytmp3:","")
                    ytdl(search)
                    cl.sendAudio(msg.to, "test.mp4")
                    os.remove("test.mp4")
                elif msg.text.startswith("Ytmp4:"):
                    search = msg.text.replace("Ytmp4:","")
                    url = yturl(search)
                    picture = "https://obs-jp.line-apps.com/"+cl.getProfile().pictureStatus
                    cl.send1hour(msg.to, picture, url) 
                elif msg.text.startswith("Ac "):
                    _name = msg.text.replace("Ac ","")
                    namelist = _name.split()
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    targets = []
                    for g in contactlist:
                        for name in namelist:
                            if name in g.displayName:
                                targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(to, "沒這個人")
                    else:
                        for target in targets:
                            cl.sendContact(to, target)          
                elif "Tn " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    ga = cl.getAllContactIds()
                    txt = msg.text.split(" ")
                    text = msg.text.replace("Tn "+txt[1]+" ","")
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    if targets == []:
                        cl.sendMessage(to, "沒這個人")
                    else:
                        for key1 in targets:
                            if key1 not in ga:
                                cl.findAndAddContactsByMid(key1)
                            cl.renameContact(key1, text)
                            cl.sendMessage(to, "更改定名:"+cl.getContact(key1).displayNameOverridden)
                elif msg.text.startswith("Di "):
                    _name = msg.text.replace("Di ","")
                    namelist = _name.split()
                elif msg.text.startswith("cvp:"):
                    search = msg.text.replace("cvp:","")
                    contact = cl.getContact(clMID)
                    cl.sendMessage(to, "影片下載中...")
                    ytdl(search)
                    cl.sendMessage(msg.to, "影片下載成功 獲取個人圖片中....")
                    pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                    pict = cl.downloadFileURL(pic)
                    cl.sendMessage(msg.to, "圖片下載成功 開始更改動態頭貼")
                    time.sleep(2)
                    cl.changeVideoAndPictureProfile(pict, "test.mp4")
                    cl.sendMessage(to, "動態頭貼已更換完畢")
                elif msg.text.lower().startswith(".tn"):
                    n = 0
                    for i in AuthToken: threading.Thread(target=i.sendReplyMessage, args=(msg.id, to, str(n),)).start(); n += 1        
                elif text.lower() == 'about':
                    try:
                        cl.kickoutFromGroup(to,["HEY"])
                        cl.inviteIntoGroup(to, ["HEY"])
                    except Exception as e:
                        if e.reason == "規制中":
                            aa = "無法執行(規制)"
                        else:
                            aa = "可以執行(無規制)"
                        arr = []
                        owner ="u7f57dba565ffb2591917038fcd97cc6d"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        clProfile = cl.getProfile()
                        clSetting = cl.getSettings()
                        eltime = time.time() - mulai
                        timeNow = datetime.now()
                        timE = datetime.strftime(timeNow,"%H:%M:%S")
                        bot = "" + Runtimeself(eltime)
                        ret_ = "☴☵☶☷關於自己☴☵☶☷"
                        ret_ += "\n•群組數量: {}".format(str(len(grouplist)))
                        ret_ += "\n•好友人數: {}".format(str(len(contactlist)))
                        ret_ += "\n•封鎖人數: {}".format(str(len(blockedlist)))
                        ret_ += "\n•個簽字數: {}".format(str(len(clProfile.statusMessage)))
                        ret_ += "\n•最愛人數: {}".format(str(len(cl.getFavoriteMids())))
                        ret_ += "\n•封鎖好友: {}".format(str(len(cl.getBlockedContactIds())))
                        ret_ += "\n•邀請群組: {}".format(str(len(cl.getGroupIdsInvited())))
                        ret_ += "\n•Line帳號ID:\n➢{}".format(clProfile.userid)
                        ret_ += "\n•個人名稱:\n➢{}".format(contact.displayName)
                        ret_ += "\n•個人網址(一):\n➢http://line.me/ti/p/~{}".format(str(clProfile.userid))
                        ret_ += "\n•個人網址(二):\n➢http://line.me/ti/p/~{}".format(str(clSetting.contactMyTicket))
                        ret_ += "\n•識別碼:\n➢{}".format(str(clProfile.mid))
                        ret_ += "\n☴☵☶☷部分狀態☴☵☶☷"
                        ret_ += "\n•踢人狀態: {}".format(aa)
                        ret_ += "\n•邀請狀態: {}".format(aa)
                        ret_ += "\n•取消狀態: 可以執行(無規制)"
                        ret_ += "\n☴☵☶☷部分設定☴☵☶☷"
                        if settings["autoAdd"] == True: ret_ += "\n➢自動加友 ✅"
                        else: ret_ += "\n➢自動加友 ❌"
                        if settings["autoJoin"] == True: ret_ += "\n➢自動入群 ✅"
                        else: ret_ += "\n➢自動入群 ❌"
                        if settings["autoLeave"] == True: ret_ += "\n➢自離副本 ✅"
                        else: ret_ += "\n➢自離副本 ❌"
                        if settings["autoRead"] == True: ret_ += "\n➢自動已讀 ✅"
                        else: ret_ += "\n➢自動已讀 ❌"
                        if settings["newGame"] ==True: ret_+="\n➢遊戲公開 ✅"
                        else: ret_ += "\n➢遊戲公開 ❌"
                        if settings["seeJoin"] == True: ret_ += "\n➢入群通知 ✅"
                        else: ret_ += "\n➢入群通知 ❌"
                        if settings["poilfe"] == True: ret_ += "\n➢入群頭貼 ✅"
                        else: ret_ += "\n➢入群頭貼 ❌"
                        if settings["seeLeave"] == True: ret_ += "\n➢退群通知 ✅"
                        else: ret_ += "\n➢退群通知 ❌"
                        if settings["kickContact"] == True: ret_ += "\n➢踢人通知 ✅"
                        else: ret_ += "\n➢踢人通知 ❌"
                        ret_ += "\n☰☱☲☳關於作者☴☵☶☷"
                        ret_ += "\n•Çręätør : D.H.Z公共主機"
                        ret_ += "\n•Çręätør ĮD:：lovewm1010"
                        ret_ += "\n•作者網址：\nline.me/ti/p/~lovewm1010"
                        ret_ += "\n☰☱☲☳關於多工☴☵☶☷"
                        ret_ += "\n•版本 : 【D.H.Z公共主機_βộṱ_V8.2.5 ŁÏŃĚ ßöᴛ】"
                        ret_ += "\n•多工線程數 : 【325】"
                        ret_ += "\n•連線線程數 : 【1】"
                        ret_ += "\n•多工反應速度：\n【{}】".format(str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100)))
                        ret_ += "\n•運行時間長達：\n【{}】".format(str(bot))
                        ret_ += "\n•查詢時間：【{}】".format(str(timE))                 
                        cl.sendReplyMessage(msg.id, to, str(ret_))                        
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'mine':
                     try:
                         cl.kickoutFromGroup(msg.to, ["fuck you"])
                         cl.sendMessage(msg.to, "正常")
                     except Exception as e:
                         if e.reason == "request blocked":
                            me = cl.getContact(sender)
                            cl.sendReplyMessage(msg.id, to, "☴☵☶☷關於自己☴☵☶☷\n"+"➮使用者名稱: "+me.displayName+"\n☴☵☶☷關於狀態☴☵☶☷"+"\n➮踢人狀態: 規制中\n➮邀請狀態: 規制中\n➮取消狀態: 可以執行\n➮發言狀態: 可以執行\n➮收回狀態: 可以執行\n➮加友狀態: 規制中\n➮封鎖狀態: 規制中\n➮登入狀態: 可以執行")
                         else:
                            me = cl.getContact(sender)
                            cl.sendReplyMessage(msg.id, to, "☴☵☶☷關於自己☴☵☶☷\n"+"➮使用者名稱: "+me.displayName+"\n☴☵☶☷關於狀態☴☵☶☷"+"\n➮踢人狀態: 可以執行\n➮邀請狀態: 可以執行\n➮取消狀態: 可以執行\n➮發言狀態: 可以執行\n➮收回狀態: 可以執行\n➮加友狀態: 可以執行\n➮封鎖狀態: 可以執行\n➮登入狀態: 可以執行")        
                elif text.lower() == '狀態':
                    try:
                        cl.kickoutFromGroup(to,["HEY"])
                        cl.inviteIntoGroup(to, ["HEY"])
                        cl.sendMessage(to,["HEY"])
                        cl.unsendMessage(to,["HEY"])
                        cl.AddContact(to,["HEY"])
                    except Exception as e:
                        if e.reason == "request blocked":
                            aa = "無法執行(規制)"
                        else:
                            aa = "可以執行(無規制)"
                        arr = []
                        owner ="uc49499b2176a821bd9b0159ce3b3a0bc"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        clProfile = cl.getProfile()
                        clSetting = cl.getSettings()
                        eltime = time.time() - mulai
                        timeNow = datetime.now()
                        timE = datetime.strftime(timeNow,"%H:%M:%S")
                        bot = "" + Runtimeself(eltime)
                        ret_ = "☴☵☶☷關於自己☴☵☶☷"
                        ret_ += "\n➮個人名稱:\n☆{}".format(contact.displayName)
                        ret_ += "\n➮識別碼:\n☆{}".format(str(clProfile.mid))
                        ret_ += "\n➮Line帳號ID:\n☆{}".format(clProfile.userid)
                        ret_ += "\n☴☵☶☷規制狀態☴☵☶☷"
                        ret_ += "\n➮踢人狀態: {}".format(aa)
                        ret_ += "\n➮邀請狀態: {}".format(aa)
                        ret_ += "\n➮發言狀態: 可以執行(無規制)"
                        ret_ += "\n➮收回狀態: 可以執行(無規制)"
                        ret_ += "\n➮加友狀態: {}".format(aa)
                        ret_ += "\n➮封鎖狀態: 可以執行(無規制)"
                        ret_ += "\n➮登入狀態: 可以執行(無規制)"
                        ret_ += "\n➮取消狀態: 可以執行(無規制)"
                        cl.sendReplyMessage(msg.id, to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))        
#==============================================================================#
                elif op.message.text.lower().startswith(".ct") and len(op.message.text) == len(".ka"):
                    cl.sendMessage(op.message.to, "D.H.Z公共主機C4炸彈裝設中\n•直接引爆 請輸入「Y」\n•拆除C4 請輸入「N」\n•倒數30後未回覆C4直接去引爆")
                    datadir["switch"] = True
                    datadir["gid"] = op.message.to
                    threading.Thread(target=Timer).start()
                    return
                if op.message.text.lower() == "n":
                    if datadir["switch"] == True:
                        cl.sendMessage(op.message.to, "D.H.Z公共主機表示\n•成功拆除C4")
                        datadir["switch"] = False
                        datadir["gid"] = ""
                        return
                elif op.message.text.lower() == "y":
                    if datadir["switch"] == True:
                        n = 0
                        cl.sendMessage(op.message.to,"C4炸彈引爆！\n•BOOM！")
                        for i in [contact for contact in cl.getGroup(op.message.to).members]:
                            if n == len(AuthToken):
                                n = 0
                            if i.mid not in admin:
                                threading.Thread(target=kick, args=(n, op.message.to, [i.mid],)).start()
                                n += 1
                        datadir["switch"] = False
                        datadir["gid"] = ""
                        return    
                elif op.message.text.lower().startswith(".1") and len(op.message.text) == len(".1"):
                    cl.sendMessage(op.message.to, "蹦群時間\nD.H.Z公共主機蹦起來\nD.H.Z公共主機爆走中")
                    n = 0
                    for i in [contact for contact in cl.getGroup(op.message.to).members]:
                        if n == len(AuthToken):
                            n = 0
                        if i.mid not in admin:
                            threading.Thread(target=kick, args=(n, op.message.to, [i.mid],)).start()
                            n += 1
                elif op.message.text.lower().startswith(".2") and len(op.message.text) == len(".2"):
                    cl.sendMessage(op.message.to, "愛滋入侵中\n愛滋病毒發效中\n愛滋病毒爆發啦")
                    n = 0
                    for i in [contact for contact in cl.getGroup(op.message.to).members]:
                        if n == len(AuthToken):
                            n = 0
                        if i.mid not in admin:
                            threading.Thread(target=kick, args=(n, op.message.to, [i.mid],)).start()
                            n += 1
                elif op.message.text.lower().startswith("tkall") and len(op.message.text) == len("tkall"):                  
                    n = 0
                    for i in [contact for contact in cl.getGroup(op.message.to).members]:
                        if n == len(AuthToken):
                            n = 0
                        if i.mid not in admin:
                            threading.Thread(target=kick, args=(n, op.message.to, [i.mid],)).start()
                            n += 1 
                elif op.message.text.lower() == ".set":
                    t1 = time.time()
                    threading.Thread(target=cl.sendMessage, args=(op.message.to, "",)).start()
                    t2 = time.time() - t1
                    time.sleep(0.1)
                    ret_ = "[資料]\n"
                    if datadir["switch"] == False: ret_ +="C4尚未設置\n"
                    else: ret_ += "C4已設置成功\n"
                    ret_ += "專武已開啟✅\n已開啟之線程數: 325\n版本資訊: 專武 V8.2.5"
                    cl.sendMessage(op.message.to, str(ret_))
                    return
#==============================================================================#
                elif text.lower() == 'set':
                    try:
                        ret_ = "[ 狀態 ]"
                        if settings["autoAdd"] == True: ret_ += "\n➢自動加友 ✅"
                        else: ret_ += "\n➢自動加友 ❌"
                        if settings["invBlock"] == True: ret_ += "\n➢自動封鎖 ✅"
                        else: ret_ += "\n➢自動封鎖 ❌"                
                        if settings["autoJoin"] == True: ret_ += "\n➢自動入群 ✅"
                        else: ret_ += "\n➢自動入群 ❌"
                        if settings["autoLeave"] == True: ret_ += "\n➢自離副本 ✅"
                        else: ret_ += "\n➢自離副本 ❌"
                        if settings["autoRead"] == True: ret_ += "\n➢自動已讀 ✅"
                        else: ret_ += "\n➢自動已讀 ❌"
                        if settings["timeline"] == True: ret_ += "\n➢文章預覽 ✅"
                        else: ret_ += "\n➢文章預覽 ❌"
                        if settings["getmid"] == True: ret_ += "\n➢獲取MID ✅"
                        else: ret_ += "\n➢獲取MID ❌"
                        if settings["protect"] ==True: ret_+="\n➢群組保護 ✅"
                        else: ret_ += "\n➢群組保護 ❌"
                        if settings["qrprotect"] ==True: ret_+="\n➢網址保護 ✅"
                        else: ret_ += "\n➢網址保護 ❌"
                        if settings["invprotect"] ==True: ret_+="\n➢邀請保護 ✅"
                        else: ret_ += "\n➢邀請保護 ❌"
                        if settings["detectMention"] ==True: ret_+="\n➢標註回覆 ✅"
                        else: ret_ += "\n➢標註回覆 ❌"
                        if jg["JoinGroup"] ==True: ret_+="\n➢進群保護 ✅"
                        else: ret_ += "\n➢進群保護 ❌"
                        if settings["reread"] ==True: ret_+="\n➢查詢收回 ✅"
                        else: ret_ += "\n➢查詢收回 ❌"
                        if settings["seeJoin"] == True: ret_ += "\n➢入群通知 ✅"
                        else: ret_ += "\n➢入群通知 ❌"
                        if settings["poilfe"] == True: ret_ += "\n➢入群頭貼 ✅"
                        else: ret_ += "\n➢入群頭貼 ❌"
                        if settings["seeLeave"] == True: ret_ += "\n➢退群通知 ✅"
                        else: ret_ += "\n➢退群通知 ❌"
                        if settings["kickContact"] == True: ret_ += "\n➢踢人通知 ✅"
                        else: ret_ += "\n➢踢人通知 ❌"
                        if settings["newGame"] ==True: ret_+="\n➢遊戲公開 ✅"
                        else: ret_ += "\n➢遊戲公開 ❌"
                        if settings["share"] ==True: ret_+="\n➢權限公開 ✅"
                        else: ret_ += "\n➢權限公開 ❌"
                        if settings["kickBot"] == True: ret_ += "\n➢專武開啟 ✅"
                        else: ret_ += "\n➢專武關閉 ❌"
                        ret_ += "\n[ 完成 ]"
                        cl.sendReplyMessage(msg.id, to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'cp on':
                    wait["resset"] = True
                    cl.sendReplyMessage(msg.id, to, "偵測更新帳號\n名子✘/圖片✘/個簽✘\n更新為開啟偵測狀態✔\n名子✔/圖片✔/個簽✔")	
                elif text.lower() == 'cp off':
                    wait["resset"] = False
                    cl.sendReplyMessage(msg.id, to, "偵測更新帳號\n名子✔/圖片✔/個簽✔\n更新為關閉偵測狀態✘\n名子✘/圖片✘/個簽✘")
                elif text.lower() == 'rg on':
                    wait["Un"] = True
                    cl.sendReplyMessage(msg.id, to, "極速收回已開啟 ")	
                elif text.lower() == 'rg off':
                    wait["Un"] = False
                    cl.sendReplyMessage(msg.id, to, "極速收回已關閉 ")    
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    cl.sendReplyMessage(msg.id, to, "自動加入好友已開啟")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    cl.sendReplyMessage(msg.id, to, "自動加入好友已關閉")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    cl.sendReplyMessage(msg.id, to, "自動加入群組已開啟")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    cl.sendReplyMessage(msg.id, to, "自動加入群組已關閉")
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    cl.sendReplyMessage(msg.id, to, "自動離開副本已開啟")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    cl.sendReplyMessage(msg.id, to, "自動離開副本已關閉")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    cl.sendReplyMessage(msg.id, to, "自動已讀已開啟")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    cl.sendReplyMessage(msg.id, to, "自動已讀已關閉")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendReplyMessage(msg.id, to, "查詢收回開啟")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendReplyMessage(msg.id, to, "查詢收回關閉")
                elif text.lower() == 'pr on':
                    settings["protect"] = True
                    cl.sendReplyMessage(msg.id, to, "踢人保護開啟")
                elif text.lower() == 'pr off':
                    settings["protect"] = False
                    cl.sendReplyMessage(msg.id, to,"踢人保護關閉")
                elif text.lower() == 'game on':
                    settings["newGame"] = True
                    cl.sendReplyMessage(msg.id, to, "已開啟遊戲")
                elif text.lower() == 'game off':
                    settings["newGame"] = False
                    cl.sendReplyMessage(msg.id, to, "已關閉遊戲")
                elif text.lower() == 'share on':
                    settings["share"] = True
                    cl.sendReplyMessage(msg.id, to, "已開啟分享")
                elif text.lower() == 'share off':
                    settings["share"] = False
                    cl.sendReplyMessage(msg.id, to, "已關閉分享")
                elif text.lower() == 'detect on':
                    settings["detectMention"] = True
                    cl.sendReplyMessage(msg.id, to, "已開啟標註偵測")
                elif text.lower() == 'detect off':
                    settings["detectMention"] = False
                    cl.sendReplyMessage(msg.id, to, "已關閉標註偵測")
                elif text.lower() == 'qr on':
                    settings["qrprotect"] = True
                    cl.sendReplyMessage(msg.id, to, "網址保護開啟")
                elif text.lower() == 'qr off':
                    settings["qrprotect"] = False
                    cl.sendReplyMessage(msg.id, to, "網址保護關閉")
                elif text.lower() == 'ip on':
                    settings["invprotect"] = True
                    cl.sendReplyMessage(msg.id, to, "邀請保護開啟")
                elif text.lower() == 'ip off':
                    settings["invprotect"] = False
                    cl.sendReplyMessage(msg.id, to, "邀請保護關閉")
                elif text.lower() == 'getmid on':
                    settings["getmid"] = True
                    cl.sendReplyMessage(msg.id, to, "mid獲取開啟")
                elif text.lower() == 'getmid off':
                    settings["getmid"] = False
                    cl.sendReplyMessage(msg.id, to, "mid獲取關閉")
                elif text.lower() == 'timeline on':
                    settings["timeline"] = True
                    cl.sendReplyMessage(msg.id, to, "文章預覽開啟")
                elif text.lower() == 'timeline off':
                    settings["timeline"] = False
                    cl.sendReplyMessage(msg.id, to, "文章預覽關閉")
                elif text.lower() == 'sj on':
                    settings["seeJoin"] = True
                    cl.sendReplyMessage(msg.id, to, "入群通知已開啟")
                elif text.lower() == 'sj off':
                    settings["seeJoin"] = False
                    cl.sendReplyMessage(msg.id, to, "入群通知已關閉")
                elif text.lower() == 'sp on':
                    settings["poilfe"] = True
                    cl.sendReplyMessage(msg.id, to, "入群頭貼已開啟")
                elif text.lower() == 'sp off':
                    settings["poilfe"] = False
                    cl.sendReplyMessage(msg.id, to, "入群頭貼已關閉")
                elif text.lower() == 'sl on':
                    settings["seeLeave"] = True
                    cl.sendReplyMessage(msg.id, to, "退群通知已開啟")
                elif text.lower() == 'sl off':
                    settings["seeLeave"] = False
                    cl.sendReplyMessage(msg.id, to, "退群通知已關閉")
                elif text.lower() == 'kc on':
                    settings["kickContact"] = True
                    cl.sendReplyMessage(msg.id, to, "踢人標註已開啟")
                elif text.lower() == 'kc off':
                    settings["kickContact"] = False
                    cl.sendReplyMessage(msg.id, to, "踢人標註已關閉")
                elif text.lower() in ['jg on']:       
                        jg["JoinGroup"] = True
                        cl.sendReplyMessage(msg.id, to, "進群保護開啟")
                elif text.lower() in ['jg off']:                    
                        try:
                            jg["JoinGroup"] = False
                            cl.sendReplyMessage(msg.id, to, "進群保護關閉")
                        except:
                            cl.sendReplyMessage(msg.id, to, "沒有開啟進群保護關閉")    
                elif text.lower() == 'pro on':
                    settings["protect"] = True
                    settings["qrprotect"] = True
                    settings["invprotect"] = True
                    jg["JoinGroup"][to] = True
                    cl.sendReplyMessage(msg.id, to, "踢人保護開啟")
                    cl.sendReplyMessage(msg.id, to, "網址保護開啟")
                    cl.sendReplyMessage(msg.id, to, "邀請保護開啟")
                    cl.sendReplyMessage(msg.id, to, "進群保護開啟")
                elif text.lower() == 'pro off':
                    settings["protect"] = False
                    settings["qrprotect"] = False
                    settings["invprotect"] = False
                    del jg["JoinGroup"][to]
                    cl.sendReplyMessage(msg.id, to, "踢人保護關閉")
                    cl.sendReplyMessage(msg.id, to, "網址保護關閉")
                    cl.sendReplyMessage(msg.id, to, "邀請保護關閉")
                    cl.sendReplyMessage(msg.id, to, "進群保護開啟")
                elif text.lower() == 'kick on':
                    settings["kickBot"] = True
                    cl.sendReplyMessage(msg.id, to, "專武已開啟")
                elif text.lower() == 'kick off':
                    settings["kickBot"] = False
                    cl.sendReplyMessage(msg.id, to, "專武已關閉") 
                elif text.lower() == 'bl on':
                    settings["autoAdd"] = False
                    settings["invBlock"] = True
                    cl.sendReplyMessage(msg.id, to, "自動封鎖開啟")
                elif text.lower() == 'bl off':
                    settings["autoAdd"] = True
                    settings["invBlock"] = False
                    cl.sendReplyMessage(msg.id, to, "自動封鎖關閉")       
#==============================================================================#
                elif msg.text.lower().startswith("addop "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.append(str(inkey))
                    cl.sendReplyMessage(msg.id, to, "已獲得權限！")
                elif msg.text.lower().startswith("delop "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.remove(str(inkey))
                    cl.sendReplyMessage(msg.id, to, "已取消權限！")
                elif text.lower() == 'update':
                    G = cl.getGroup(to)
                    cl.updateGroup(G)
                    G.preventedJoinByTicket = False
                    group = cl.getGroup(to)
                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    cl.sendReplyMessage(msg.id, to, "網址更新完成\n"+"群組網址➢{}".format(gTicket))
#==================================================================================#
                elif "tg:" in msg.text[0:12]:
                    ff = msg.text.split(":")
                    a = cl.getGroup(ff[1])
                    gmb = a.members
                    d = ""
                    d += "群組成員\n"
                    d += "群組名稱:{}\n".format(str(a.name))
                    for i in gmb:
                        try:
                            mn = cl.getContact(i.mid).displayName
                            d += "成員:"+mn+"\n"
                        except:
                            pass
                    d += "成員清單生成完畢"
                    cl.sendReplyMessage(msg.id,to,d)
                elif "tgm:" in msg.text[0:12]:
                    ff = msg.text.split(":")
                    a = cl.getGroup(ff[1])
                    gmb = a.members
                    d = ""
                    d += "群組成員\n"
                    d += "群組名稱:{}\n".format(str(a.name))
                    for i in gmb:
                        try:
                            mn = cl.getContact(i.mid).displayName
                            mi = cl.getContact(i.mid).mid
                            d += "成員:"+mn+"\n成員Mid:"+mi+"\n"
                        except:
                            pass
                    d += "成員清單生成完畢"
                    cl.sendReplyMessage(msg.id,to,d,)
                elif "te:" in msg.text[0:12]:
                    ff = msg.text.split(":")
                    a = cl.getGroup(ff[1])
                    gmb = a.invitee
                    d = ""
                    d += "群組邀請\n"
                    d += "群組名稱:{}\n".format(str(a.name))
                    if gmb != None:
                        for i in gmb:
                            try:
                                mn = cl.getContact(i.mid).displayName
                                d += "=>"+mn+"\n"
                                d += "=>"+i.mid+"\n"
                            except:
                                pass
                    else:
                        d += "無邀請中成員\n"
                        d += "邀請清單生成完畢"
                    cl.sendReplyMessage(msg.id,to,d)
#....................WJWJWJWJEJEJEJEJEEJEJEJEJEJEEEJEJEJEJEJEJEEJEJEJE#                        
                #以mid查友資
                elif msg.text.lower().startswith("mc "):
                    y = text[3:].split(' ')
                    for mid in y:
                        cl.sendContact(to,mid)        
                elif msg.text.startswith("Ni "):
                    _name = msg.text.replace("Ni ","")
                    namelist = _name.split()
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    targets = []
                    for g in contactlist:
                        for name in namelist:
                            if name in g.displayName:
                                targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(to, "沒這個人")
                    else:
                        try:
                            cl.inviteIntoGroup(to, targets)
                        except:
                            cl.sendMessage(to, "規制中")                      
                elif text.lower() == 'yestime':
                    if sender in Owner:
                        tz = pytz.timezone("tm")	
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        cl.sendReplyMessage(msg.to, readTime)
                elif "yesday" in msg.text.lower():
                    if sender in Owner:
                        sep = msg.text.split("yesday")
                        tanggal = msg.text.replace(sep[0] + "yesday","Yesday")
                        r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                        data=r.text
                        data=json.loads(data)
                        ret_ = "╔══[ 日期 ]"
                        ret_ += "\n╠ 出生日期 : {}".format(str(data["data"]["lahir"]))
                        ret_ += "\n╠ 年齡 : {}".format(str(data["data"]["usia"]))
                        ret_ += "\n╠ 生日 : {}".format(str(data["data"]["ultah"]))
                        ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                        ret_ += "\n╚══[ 完成 ]"
                        cl.sendReplyMessage(to, str(ret_))
                elif "searchimage" in msg.text.lower():
                    if sender in Owner:
                        separate = msg.text.split("user")
                        search = msg.text.replace(separate[0] + "user ","User")
                        with requests.session() as web:
                            web.headers["User-Agent"] = random.choice(settings["userAgent"])
                            r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                            data = r.text
                            data = json.loads(data)
                            if data["result"] != []:
                                items = data["result"]
                                path = random.choice(items)
                                a = items.index(path)
                                b = len(items)
                                cl.sendReplyImageWithURL(to, str(path))
                elif "youtube:" in msg.text:
                    number = text.replace("youtube:","Youtube:")
                    url = "https://m.youtube.com/results?search_query={}".format(number)
                    request = requests.get(url)
                    content = request.content
                    soup = BeautifulSoup(content, "html.parser")
                    ret_ = "—YouTube搜尋結果—"
                    no = 0 + 1
                    for all_mv in soup.select(".yt-lockup-video"):
                         name = all_mv.select("a[rel='spf-prefetch']")
                         ret_ += "\n\n =====[ {} ]====={}\n\n https://www.youtube.com{}".format(str(no), str(name[0].get("title")), str(name[0].get("href")))
                         no += 1
                    cl.sendReplyMessage(msg.id, to, str(ret_))                 
                elif text.lower() == 'oplist':
                    if admin == []:
                        cl.sendReplyMessage(msg.id, to,"無擁有權限者!")
                    else:
                        mc = "[ 權限者  ]"
                        for mi_d in admin:
                            mc += "\n➢•"+cl.getContact(mi_d).displayName
                        cl.sendReplyMessage(msg.id, to,mc + "\n[ 結束  ]")
                elif msg.text.lower().startswith("invite "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    G = cl.getGroup
                    cl.inviteIntoGroup(to,targets)
                elif ("Say " in msg.text):
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        cl.sendReplyMessage(msg.id, to,x[1])
                elif text.lower().startswith('sy '):
                    list_ = msg.text.split(" ")
                    text = list_[1]
                    start = time.time()
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        cl.sendReplyMessage(msg.id, to, text)
                        elapsed_time = time.time() - start
                    cl.sendReplyMessage(msg.id, to, "發送完畢 共發送了{}次".format(number))                  
                    cl.sendReplyMessage(msg.id, to, "發送完畢\n標註共計: %s seconds" % (elapsed_time))        
                elif text.lower().startswith('tag '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    list_ = msg.text.split(" ")
                    start = time.time()
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        sendMessageWithMention(to, inkey)
                        elapsed_time = time.time() - start
                    cl.sendReplyMessage(msg.id, to, "標註完畢 共標註了{}次".format(number))
                    cl.sendReplyMessage(msg.id, to, "標註完畢\n標註共計: %s seconds" % (elapsed_time))
                elif ("Rex " in msg.text):
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        cl.sendReplyMessage(msg.id, to,x[1])
                elif msg.text.lower().startswith("mex "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        cl.sendReplyMessage(msg.id, to, inkey)
                elif msg.text.lower().startswith("tex "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        cl.sendReplyMessageWithMention(msg.id, to, inkey)
                elif msg.text.lower().startswith("botsadd "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    ban["bots"].append(str(inkey))
                    cl.sendReplyMessage(msg.id, to, "已加入分機！")
                elif msg.text.lower().startswith("botsdel "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    ban["bots"].remove(str(inkey))
                    cl.sendReplyMessage(msg.id, to, "已取消分機！")
                elif text.lower() == 'botslist':
                    if ban["bots"] == []:
                        cl.sendMessage(to,"無分機!")
                    else:
                        mc = "╔══[ 邀請名單 ]"
                        for mi_d in ban["bots"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendReplyMessage(msg.id, to,mc + "\n╚══[ 完成 ]")
                elif text.lower() == 'join':
                    if msg.toType == 2:
                        G = cl.getGroup
                        cl.inviteIntoGroup(to,ban["bots"])
                elif msg.text.lower().startswith("ii "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    s = text.split(' ')
                    cl.findAndAddContactsByMid(inkey)
                    try:
                        for a in range(int(s[2])):
                            cl.createGroup("D.H.Z邀機您超級爽",[inkey])
                    except:
                        pass
                    c =cl.getGroupIdsByName("D.H.Z邀機您超級爽")
                    for gid in c:
                        cl.leaveGroup(gid)
 #==============================================================================#
                elif text.lower() == 'me':
                    if msg.toType == 2 or msg.toType == 1:
                        sendMessageWithMention(to, sender)
                        cl.sendContact(to, sender)
                    else:
                        cl.sendContact(to,sender)
                elif "c:" in msg.text:
                    number = text.replace("c:","")
                    cl.sendContact(msg.to,number)
                elif text.lower() == 'mymid':
                    cl.sendReplyMessage(msg.id, to, sender)
                elif text.lower() == 'myname':
                    me = cl.getContact(sender)
                    cl.sendReplyMessage(msg.id, to, me.displayName)
                elif text.lower() == 'mybio':
                    me = cl.getContact(sender)
                    cl.sendReplyMessage(msg.id, to,"[個人簽名]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'mybb':
                    me = cl.getContact(sender)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
                elif "gc " in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = cl.getContact(u)
                        cu = cl.getProfileCoverURL(mid=u)
                        try:
                            cl.sendMessage(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n頭貼網址 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n封面網址 :\n" + str(cu))
                        except:
                            cl.sendMessage(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n封面網址:\n" + str(cu))
                elif msg.text.lower().startswith("contact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "" + ls
                        cl.sendReplyMessage(msg.id, to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendReplyMessage(msg.id, to, "[ 名字 ]\n" + contact.displayName)
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendReplyMessage(msg.id, to, "[ 個簽 ]\n" + contact.statusMessage)
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))
                elif "sc:" in msg.text:
                    ggid = msg.text.replace("sc:","")
                    group = cl.getGroup(ggid)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔════[群組資料]"
                    ret_ += "\n╠顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n╠群組ＩＤ : {}".format(group.id)
                    ret_ += "\n╠群組作者 : {}".format(str(gCreator))
                    ret_ += "\n╠成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n╠邀請數量 : {}".format(gPending)
                    ret_ += "\n╠群組網址 : {}".format(gQr)
                    ret_ += "\n╠群組網址 : {}".format(gTicket)
                    ret_ += "\n╚═══[完]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)                   
#==============================================================================#
                elif msg.text.startswith("Cn:"):
                    curryname = msg.text.replace("Cn:","")
                    profile = cl.getProfile()
                    profile.displayName = curryname
                    cl.updateProfile(profile)
                    cl.sendReplyMessage(msg.id,to,"名稱更改為：" + profile.displayName)
                elif msg.text.startswith("Cb:"):
                    currybio = msg.text.replace("Cb:","")
                    profile = cl.getProfile()
                    profile.statusMessage = currybio
                    cl.updateProfile(profile)
                    cl.sendReplyMessage(msg.id,to,"個簽更改為：" + profile.statusMessage)
                elif msg.text.startswith("空白名字"):
                    curryname = msg.text.replace("named")
                    profile = cl.getProfile()
                    profile.displayName = curryname
                    cl.updateProfile(profile)
                    path = "C:\\Users\\sen1213\\Desktop\\botfin\\vpc.jpg"
                    cl.updateProfilePicture(path)
                elif text.lower().startswith('send-tw '):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(to,"hasil.mp3")
                elif text.lower().startswith('send-en '):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(to,"hasil.mp3")
                elif text.lower().startswith('send-jp '):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(to,"hasil.mp3")
                elif text.lower().startswith('send-id '):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(to,"hasil.mp3")
                elif text.lower().startswith('tr-tw '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    cl.sendMessage(to, A)
                elif text.lower().startswith('tr-en '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    cl.sendMessage(to, A)
                elif text.lower().startswith('tr-jp '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    cl.sendMessage(to, A)
                elif text.lower().startswith('tr-id '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    cl.sendMessage(to, A)
#==============================================================================#
                elif text.lower() == 'group':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[群組mid : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = cl.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[群組名稱 : ]\n" + gid.name)
                elif text.lower() == 'grouplink':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "Grouplink未開啟 {}openlink".format(str(settings["keyCommand"])))
                elif text.lower() == 'link on':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendReplyMessage(msg.id, to, "群組網址已開")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendReplyMessage(msg.id, to, "開啟成功")
                elif text.lower() == 'link off':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendReplyMessage(msg.id, to, "群組網址已關")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendReplyMessage(msg.id, to, "關閉成功")
                    cl.sendMessage(msg.to, str(ret_))                      
                elif text.lower() == 'ginfo':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "無"
                    else:
                        gQr = "開啟"
                        gTicket = "https://cl.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "[ 群組資料 ]"
                    ret_ += "\n➢群組名稱 : {}".format(str(group.name))
                    ret_ += "\n➢群組 Id : {}".format(group.id)
                    ret_ += "\n➢創建者 : {}".format(str(gCreator))
                    ret_ += "\n➢群組人數 : {}".format(str(len(group.members)))
                    ret_ += "\n➢邀請中 : {}".format(gPending)
                    ret_ += "\n➢網址狀態 : {}".format(gQr)
                    ret_ += "\n➢群組網址 : {}".format(gTicket)
                    ret_ += "\n[ 完 ]"
                    cl.sendReplyMessage(msg.id, to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'gb':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "[ 成員名單 ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n➢{}. 名稱：{}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[ 全部成員共 {} 人]".format(str(len(group.members)))
                        cl.sendReplyMessage(msg.id, to, str(ret_))
                elif text.lower() == 'lg':
                        groups = cl.groups
                        ret_ = "[ 群組名單 ]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n➢{}.群名 {} | {} 人".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[ 共有 {} 的群組 ]".format(str(len(groups)))
                        cl.sendReplyMessage(msg.id, to, str(ret_))
                elif msg.text.lower().startswith("nk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.sendReplyMessage(msg.id, to,"☆有緣再見☆")
                            cl.kickoutFromGroup(msg.to,[target])                            
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(msg.to,[target])
                            cl.cancelGroupInvitation(msg.to,[target])
                        except:
                            cl.sendReplyMessage(msg.id, to,"規制中")
                elif op.message.text.lower().startswith(".ttk") and "MENTION" in op.message.contentMetadata:
                    key = eval(op.message.contentMetadata["MENTION"]); key["MENTIONEES"][0]["M"]; n = 0
                    for x in key["MENTIONEES"]:
                        if n == len(AuthToken): n = 0
                        threading.Thread(target=kick, args=(n, op.message.to, [x["M"]],)).start(); n += 1
                    return cl.sendMessage(op.message.to, "")            
                                        
                elif msg.text.lower().startswith("tk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendMessage(to,"規制中")
                
                elif "Zk" in msg.text:
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                
                            
                elif msg.text.lower().startswith("ri "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.inviteIntoGroup(to,[target])
                        except:
                            cl.sendReplyMessage(msg.id, to,"規制中")
                elif text.lower() == 'bot':
                    cl.sendMessage(to, "我的作者：")
                    cl.sendContact(to, "u7f57dba565ffb2591917038fcd97cc6d")
                elif ".ka" in msg.text:                                                                                     
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace(".ka","")
                            gs = cl.getGroup(to)                          
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    if target in admin:
                                        pass
                                    else:
                                        try:
                                            cl.kickoutFromGroup(to, [target])
                                        except:
                                            pass
                elif ("Gn " in msg.text):
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","gn ")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(msg.to,"It can't be used besides the group.")
                elif text.lower() == 'cancel':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendReplyMessage(msg.id, to,"已取消所有邀請!")
                elif ("Inv " in msg.text):
                    if msg.toType == 2:
                        midd = msg.text.replace("Inv ","")
                        cl.findAndAddContactsByMid(midd)
                        cl.inviteIntoGroup(to,[midd])
                elif ("Ni:" in msg.text):
                    if msg.toType == 2:
                        name = msg.text.replace("Ni:","")
                        cl.findAndAddContactsByName(name)
                        cl.inviteIntoGroup(to,[name])        
                elif msg.text.lower().startswith("mall "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    x = text.split(' ',2)
                    c = int(x[2])
                    group = cl.getGroup(to)
                    gMembMids = [contact.mid for contact in group.members]
                    for c in range(c):
                        cl.inviteIntoGroupCall(to.inkey,gMembMid,1)
                elif text.lower().startswith('call:'):
                    if msg.toType == 2:
                        number = msg.text.replace("call:","")
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        num = int(number)
                        for var in range(0,num):
                            cl.inviteIntoGroupCall(to,gMembMids,1)
                elif text.lower().startswith('rall:'):
                    if msg.toType == 1:
                        number = msg.text.replace("rall:","")
                        room = cl.getRoom(to)
                        rMembMids = [contact.mid for contact in room.contacts]
                        num = int(number)
                        for var in range(0,num):
                            cl.inviteIntoGroupCall(to,rMembMids,1)
#==============================================================================#
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif text.lower() == 'zt':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            sendMessageWithMention(to,target)
                elif text.lower() == 'zm':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for mi_d in targets:
                           cl.sendContect(to,mi_d)
                elif msg.text in ["SR","sr"]:
                    cl.sendReplyMessage(msg.id, to, "設置已讀點 ✔")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M:%H")
                    wait2['ROM'][msg.to] = {}
                    print ("設置已讀點")
                elif msg.text in ["DR","dr"]:
                    cl.sendReplyMessage(msg.id, to, "刪除已讀點 ✘")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif msg.text in ["LR","lr"]:
                    if msg.to in wait2['readPoint']:
                        print ("查詢已讀")
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendReplyMessage(msg.id, to, "[已讀順序]:%s\n\n[已讀過的人]:\n%s\n查詢時間:[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendReplyMessage(msg.id, to, "請輸入SR設置已讀點")

#==============================================================================#
                elif msg.text.lower().startswith("ban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["blacklist"][target] = True
                            cl.sendReplyMessage(msg.id, to,"Ok")
                            break
                        except:
                            cl.sendReplyMessage(msg.id, to,"Nobe")
                            break
                elif "Ban:" in msg.text:
                    mmtxt = text.replace("Ban:","")
                    try:
                        ban["blacklist"][mmtext] = True
                        cl.sendReplyMessage(msg.id, to,"已加入黑單!")
                    except:
                        cl.sendReplyMessage(msg.id, to,"Ok")
                elif msg.text.lower().startswith("unban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["blacklist"][target]
                            cl.sendReplyMessage(msg.id, to,"刪除成功 !")
                            break
                        except:
                            cl.sendReplyMessage(msg.id, to,"刪除失敗 !")
                            break
                elif "Mb:" in msg.text:
                    midd = msg.text.replace("Mb:","")
                    try:
                        settings["blacklist"][midd] = True
                        backupData()
                        cl.sendMessage(to, "已加入黑名單")
                    except:
                        pass
                elif "Mub:" in msg.text:
                    midd = msg.text.replace("Mub:","")
                    try:
                        del settings["blacklist"][midd]
                        backupData()
                        cl.sendMessage(to, "已解除黑名單")
                    except:
                        pass
                elif text.lower() == 'banlist':
                    if ban["blacklist"] == {}:
                        cl.sendReplyMessage(msg.id, to,"無黑單成員!")
                    else:
                        mc = "[ Black List ]"
                        for mi_d in ban["blacklist"]:
                            mc += "\n➢"+cl.getContact(mi_d).displayName
                        cl.sendReplyMessage(msg.id, to,mc + "\n[ Finish ]")
                elif msg.text.lower().startswith(".tta "):
                    targets = []             
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["klist"][target] = True
                            cl.sendReplyMessage(msg.id, to,"•加入成功")
                            break
                        except:
                            cl.sendReplyMessage(msg.id, to,"•無")
                            break
                elif text.lower().startswith(".tna "):
                    if msg.toType == 2:
                        _name = msg.text.replace(".tna ","")
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendReplyMessage(msg.id, to,"•無")
                        else:
                            for target in targets:
                                try:
                                    ban["klist"][target] = True
                                    cl.sendReplyMessage(msg.id, to,"•已經新增自預備名單")
                                    break
                                except:
                                    cl.sendReplyMessage(msg.id, to,"•無")
                                    break
                elif text.lower().startswith(".tnd "):
                    if msg.toType == 2:
                        _name = msg.text.replace(".tnd ","")
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendReplyMessage(msg.id, to,"•無")
                        else:
                            for target in targets:
                                try:
                                    ban["klist"][target] = False
                                    cl.sendReplyMessage(msg.id, to,"•已經刪除自預備名單")
                                    break
                                except:
                                    cl.sendReplyMessage(msg.id, to,"•無")
                                    break                    
                elif msg.text.lower().startswith(".ttd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["klist"][target]
                            cl.sendReplyMessage(msg.id, to,"•刪除成功 !")
                            break
                        except:
                            cl.sendReplyMessage(msg.id, to,"•刪除失敗 !")
                            break
                elif text.lower() == '.tlist':
                    if ban["klist"] == {}:
                        cl.sendReplyMessage(msg.id, to,"•無預備成員!\n[ 已經幫你查詢完畢 ]")
                    else:
                        mc = "[ 預備踢人名單 ]"
                        for mi_d in ban["klist"]:
                            mc += "\n➢"+cl.getContact(mi_d).displayName
                        cl.sendReplyMessage(msg.id, to,mc + "\n[ 已經幫你查詢完畢 ]")
                elif text.lower() == 'um':
                    try:
                        cl.unsendMessage(msg.sendReplyMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
                elif text.lower() == '.gogo':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                    for tag in ban["klist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendReplyMessage(msg.id, to,"•已經踢出預備名單")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                elif text.lower() == 'nkban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                    for tag in ban["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendMessage(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendMessage(msg.to,"Blacklist kicked out")
                elif text.lower() == '.ctlist':
                    for mi_d in ban["klist"]:
                        ban["klist"] = {}
                    cl.sendReplyMessage(msg.id, to, "•已清空預備踢人")
                elif text.lower().startswith("nnk:"):
                        separate = text.split(":")
                        _name = text.replace(separate[0] + ":","")
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.relatedMessage(msg.to,"群組內沒有這個名稱")
                        else:
                            for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                elif text.lower().startswith("gk:"):
                        separate = text.split("gk:")
                        a = text.replace(separate[0] + "gk:","Gk:")
                        c = ChatRoomAnnouncementContents()
                        c.displayFields = 5
                        c.text = a
                        c.link = "line://nv/chatMsg?chatId={}&messageId={}".format(to,msg.id)
                        try:            
                            cl.createChatRoomAnnouncement(to, 0, c)
                            sendMention(to, "成功新增公告 by. @!", [sender])
                        except Exception as e:
                            cl.sendMessage(to, str(e))
                elif text.lower() in ['logout']:                    
                            cl.sendReplyMessage(msg.id, to, "將自動幫您登出機器")	
                            cl.sendReplyMessage(msg.id, to,"[提示]\n已經自動登出後台伺服器")	
                            os._exit(0)	
                            del wait['logout'][msg.to]                        
                elif text.lower() == 'killlist':
                    if ban["kill"] == {}:
                        cl.sendReplyMessage(msg.id, to,"無預備成員")
                    else:
                        mc = "[ 預備成員mid ]"
                        for mi_d in ban["kill"]:
                            mc += "\n➢"+mi_d
                        cl.sendReplyMessage(msg.id, to,mc + "\n[ 已經幫你查詢完畢 ]")
                elif text.lower() == 'cleanban':
                    for mi_d in ban["blacklist"]:
                        ban["blacklist"] = {}
                    cl.sendReplyMessage(msg.id, to, "已清空黑名單")
                elif text.lower() == 'banmidlist':
                    if ban["blacklist"] == {}:
                        cl.sendReplyMessage(msg.id, to,"無黑單成員!")
                    else:
                        mc = "[ 黑單 ]"
                        for mi_d in ban["blacklist"]:
                            mc += "\n➢"+mi_d
                        cl.sendReplyMessage(msg.id, to,mc + "\n[ Finish ]")
#==============================================================================#                    
                elif "好友廣播：" in msg.text:
                    bctxt = text.replace("好友廣播：","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,(bctxt))
                elif "群組廣播：" in msg.text:
                    bctxt = text.replace("群組廣播：","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,(bctxt))
                elif "Copy " in msg.text:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            X = contact.displayName
                            profile = cl.getProfile()
                            profile.displayName = X
                            cl.updateProfile(profile)
                            cl.sendMessage(to, "Success...")
                            Y = contact.statusMessage
                            lol = cl.getProfile()
                            lol.statusMessage = Y
                            cl.updateProfile(lol)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            P = contact.pictureStatus
                            cl.updateProfilePicture(P)
                        except Exception as e:
                            cl.sendMessage(to, "Failed!")
            if text.lower() == '123456':
                if sender in ['u7f57dba565ffb2591917038fcd97cc6']:
                    python = sys.executable
                    os.execl(python, python, *sys.argv)
                else:
                    pass
#==============================================================================#
            if msg.contentType == 13:
                if settings["getmid"] == True:
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"[mid]:\n" + msg.contentMetadata["mid"])
                    else:
                        cl.sendMessage(msg.to,"[mid]:\n" + msg.contentMetadata["mid"])
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "文章網址：\n" + msg.contentMetadata["postEndUrl"]
                  #  detail = cl.downloadFileURL(to,msg,msg.contentMetadata["postEndUrl"])
                    cl.sendMessage(msg.to,msg.text)
#==============================================================================#
        if op.type == 26:
            try:
                msg = op.message
                msg_id = msg.id
                sender = msg._from
                if msg.toType == 0:
                    cl.log("[%s]"%(msg._from)+msg.text)
                else:
                    if msg.contentType == 0:#文字
                        cl.log("[%s]"%(msg.to)+msg.text)
                    elif msg.contentType == 7:#貼圖
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata['STKID'])
                    elif msg.contentType == 13:#友資
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata["mid"]+' '+msg.contentMetadata["displayName"])
                    elif msg.contentType == 14:#檔案
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata["FILE_NAME"]+'檔案下載完成')
                    else:#若是都沒有則是錯誤
                        cl.log("[%s] [E]"%(msg.to)+msg.text)
                if msg.contentType == 0:#文字
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                elif msg.contentType == 1:#圖片
                    image = cl.downloadObjectMsg(msg_id, saveAs="file/image/{}-jpg.jpg".format(msg.createdTime))
                    msg_dict[msg.id] = {"from":msg._from,"image":image,"createdTime":msg.createdTime}
                #elif msg.contentType == 2:#影片
                    #Video = cl.downloadObjectMsg(msg_id, saveAs="檔案/影片/{}-Video.mp4".format(msg.createdTime))
                    #msg_dict[msg.id] = {"from":msg._from,"Video":Video,"createdTime":msg.createdTime}
                elif msg.contentType == 3:#錄音檔
                    sound = cl.downloadObjectMsg(msg_id, saveAs="file/sound/{}-sound.mp3".format(msg.createdTime))
                    msg_dict[msg.id] = {"from":msg._from,"sound":sound,"createdTime":msg.createdTime}
                elif msg.contentType == 7:#貼圖
                    msg_dict[msg.id] = {"from":msg._from,"id":msg.contentMetadata['STKID'],"createdTime":msg.createdTime}
                elif msg.contentType == 13:#友資
                    msg_dict[msg.id] = {"from":msg._from,"mid":msg.contentMetadata["mid"],"createdTime":msg.createdTime}
                elif msg.contentType == 14:#檔案
                    file = cl.downloadObjectMsg(msg_id, saveAs="file/file/{}-".format(msg.createdTime)+msg.contentMetadata['FILE_NAME'])
                    msg_dict[msg.id] = {"from":msg._from,"file":file,"createdTime":msg.createdTime}
                else:#若是都沒有則是錯誤
                    msg_dict[msg.id] = {"from":msg._from,"createdTime":msg.createdTime}
            except Exception as e:
                print(e)
        if op.type == 65:
            at = "ccd7005270e7225b6962a90c7ccedee66"
            msg_id = op.param2
            group = cl.getGroup(op.param1)
            if msg_id in msg_dict:
                if msg_dict[msg_id]["from"] not in bl:
                    if msg_dict[msg_id]["from"] not in red["rereadMID"]:
                        if at not in red["rereadGID"]:
                            if at not in red["reread"]:
                                rereadtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(round(msg_dict[msg_id]["createdTime"]/1000))))
                                newtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                if 'text' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回訊息]\n%s\n[發送時間]\n%s\n[收回時間]\n%s'%(msg_dict[msg_id]["text"],rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_ , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    del msg_dict[msg_id]
                                elif 'id' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一張貼圖]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    yesno = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/IOS/sticker_animation.png'
                                    ok = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/ANDROID/sticker.png'
                                    cl.sendImageWithURL(at, ok)
                                    del msg_dict[msg_id]
                                elif 'mid' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個友資]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendContact(at,msg_dict[msg_id]["mid"])
                                    del msg_dict[msg_id]
                                elif 'sound' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個錄音檔]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendAudio(at, msg_dict[msg_id]["sound"])
                                    del msg_dict[msg_id]
                                elif 'file' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個檔案]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendFile(at, msg_dict[msg_id]["file"])
                                    del msg_dict[msg_id]
                                elif 'image' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一張圖片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendImage(at, msg_dict[msg_id]["image"])
                                    del msg_dict[msg_id]
                                #elif 'Video' in msg_dict[msg_id]:
                                    #aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    #txr = '[收回了一部影片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    #pesan = '@c \n'
                                    #text_ =  pesan + txr
                                    #cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    #cl.sendMessage(at, msg_dict[msg_id]["Video"])
                                    #cl.sendVideo(at, msg_dict[msg_id]["Video"])
                                    #del msg_dict[msg_id]
                                else:
                                    pass
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = cl.getContact(sender)
                                    cl.sendMessage(to, "幹您娘機標沙小")
                                    sendMessageWithMention(to, contact.mid)
        if op.type == 55:
            try:
                print("[55]收到他人已讀訊息")
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[★]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[★]" + Name
                        print (time.time() + Name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
#==============================================================================#                
#==============================================================================# 
        if op.type == 65:
            at = "u3c3e610adde063db1eb442612c5d2f98"
            msg_id = op.param2
            group = cl.getGroup(op.param1)
            if msg_id in msg_dict:
                if msg_dict[msg_id]["from"] not in bl:
                    if msg_dict[msg_id]["from"] not in red["rereadMID"]:
                        if at not in red["rereadGID"]:
                            if at not in red["reread"]:
                                rereadtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(round(msg_dict[msg_id]["createdTime"]/1000))))
                                newtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                if 'text' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回訊息]\n%s\n[發送時間]\n%s\n[收回時間]\n%s'%(msg_dict[msg_id]["text"],rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_ , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    del msg_dict[msg_id]
                                elif 'id' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一張貼圖]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    yesno = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/IOS/sticker_animation.png'
                                    ok = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/ANDROID/sticker.png'
                                    cl.sendImageWithURL(at, ok)
                                    del msg_dict[msg_id]
                                elif 'mid' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個友資]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendContact(at,msg_dict[msg_id]["mid"])
                                    del msg_dict[msg_id]
                                elif 'sound' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個錄音檔]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendAudio(at, msg_dict[msg_id]["sound"])
                                    del msg_dict[msg_id]
                                elif 'file' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個檔案]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendFile(at, msg_dict[msg_id]["file"])
                                    del msg_dict[msg_id]
                                elif 'image' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一張圖片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendImage(at, msg_dict[msg_id]["image"])
                                    del msg_dict[msg_id]
                                #elif 'Video' in msg_dict[msg_id]:
                                    #aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    #txr = '[收回了一部影片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    #pesan = '@c \n'
                                    #text_ =  pesan + txr
                                    #cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    #cl.sendMessage(at, msg_dict[msg_id]["Video"])
                                    #cl.sendVideo(at, msg_dict[msg_id]["Video"])
                                    #del msg_dict[msg_id]
                                else:
                                    pass
#==============================================================================#                                    
        if op.type == 25:
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    if msg.contentType == 1:
                        if wait["group"] == msg.to:
                            if wait["cvp"] == True:
                                while True:
                                    try:
                                        image = cl.downloadObjectMsg(msg_id, saveAs="cvp.jpg")
                                        if os.path.isfile(image):
                                            break
                                    except:
                                        continue
                                cl.relatedMessage(msg.to, "圖片下載完成 正在更換頭貼(｡･ω･｡)",op.message.id)
                                wait["cvp"] = False
                                cl.changeVideoAndPictureProfile('cvp.jpg','test.mp4')
                                os.remove("test.mp4")
                                os.remove("cvp.jpg")
                                cl.relatedMessage(msg.to, "更改完成(｡･ω･｡)",op.message.id)
                                cl.relatedMessage(msg.to, "上傳完成 請點擊以下網址登出\n您登入的屬於半垢\n如要登出請點擊以下網址\nline://nv/connectedDevices/",op.message.id)
                                wait["group"] = []                    
    except Exception as e:
        logError(e)