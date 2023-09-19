#-----------------INFO----------------#
#CODING MR_NASRAT
#FACEBOOK > LOY RAYESS KABUL 
#GITHUB > Nasrat99845.git
#Join Youtobe Channel For More Cracking BRO
#https://t.me/JNRALN
## https://t.me/NASRAT YT
## TG : https://t.me/HACKIN TECH
#-------------MAIN>MENU-------------#


import marshal,os,sys,time
os.system("clear")
os.system("xdg-open https://www.facebook.com/profile.php?id=100024147440412")
os.system("xdg-open https://www.facebook.com/profile.php?id=100024147440412")
os.system("clear")
os.system("xdg-open https://www.youtube.com/@nasratYT")

    
logo = ("""\033[1;92m

$$\   $$\  $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\ $$$$$$$$\ 
$$$\  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\\__$$  __|
$$$$\ $$ |$$ /  $$ |$$ /  \__|$$ |  $$ |$$ /  $$ |  $$ |   
$$ $$\$$ |$$$$$$$$ |\$$$$$$\  $$$$$$$  |$$$$$$$$ |  $$ |   
$$ \$$$$ |$$  __$$ | \____$$\ $$  __$$< $$  __$$ |  $$ |   
$$ |\$$$ |$$ |  $$ |$$\   $$ |$$ |  $$ |$$ |  $$ |  $$ |   
$$ | \$$ |$$ |  $$ |\$$$$$$  |$$ |  $$ |$$ |  $$ |  $$ | AFG  
\__|  \__|\__|  \__| \______/ \__|  \__|\__|  \__|  \__|                                       

  \x1b[1;91m--●\x1b[1;92m━═━═━═━━═━═━═\x1b[1;91m❴\033[47m\033[1;30m HACKIN
TECH\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━━═━═━\x1b[1;91m●-- 
""")
def main():
        try:
        	   
                print (logo)
                print ('    \033[1;32m┏━━━\033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m]\033[1;32m EXAMPLE :\033[33;1m/sdcard/file.py')
                file = input ('    \033[1;32m┗━━━\033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32mFILE NAME :\033[33;1m ')
                fileopen = open(file).read()
                a = compile(fileopen, 'dg', 'exec')
                m = marshal.dumps(a)
                s = repr(m)
                b = ('##-----------------------ADMIN>INFO---------------------------##\n# ENCRYPTION BY :NASRAT\n# VERSION : 1.0\n# GITHUB : https://github.com/Nasrat99845.git\n##------------------------MAIN>MENU-------------------------##\nimport marshal\nexec(marshal.loads(' + s +'))')
                c = file.replace('.py', '.py')
                d = open(c, 'w')
                d.write(b)
                d.close()
                print ('    \033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32mENCRYPTION SUCCESSFUL >',c)
                print('    \033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                time.sleep(1)
                aq = input ('    \033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32mWANT TO ENCRYPT AGAIN? [Y/N]')
                if aq =="":
                        print ('    \033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32mCOMMAND NOT FOUND !')
                        os.sys.exit()
                elif aq =="y" or aq =="Y":
                        main()
                else:
                        if aq =="n" or aq =="N":
                                print ('    \033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32m➤THANK YOU BRO ;v\n')
                        else:
                                print ('    \033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32mCOMMAND NOT FOUND!')
                                os.sys.exit()
        except IOError:
                print ('   \033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32mFILE NOT FOUND ! ')
                time.sleep(1)
                main()

if __name__=='__main__':
        main()
