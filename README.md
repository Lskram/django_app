# django_app
การบ้านชิ้นที่ 2 Django ในรายวิชา การเขียนโปรเเกรมขั้นสูงของอาจารย์พิศาล สุขขีสุดหล่อ
1.สร้างฟังก์ชั่น  , Url เพื่อ cal back
โดย 1.1 Python manage.py startapp ชื่อแอป  (ความยากระดับง่าย)
    จะ Expo ขึ้นมาเป็นชื่อแอปที่เราตั้ง ที่ด้านซ้าย
    1.2 คลิกที่เว็บแอปที่เราสร้างขึ้นมา สร้างไฟล์ .py ว่า urls.py (ต้องมี S ด้วย)
    1.3 ไปที่ views  เพื่อ import ,HttpRespones
    1.4 สร้างเว็บขึ้นมา 3 ฟังกชั่น โดย
    def home (request):
        return HttpRespones("Hello,this my fasion ขวดน้อยเหน็บกางเกง"):

    def about(request):
        return HttpRespones("About Us"):

    def contact(request):
        reture HttpRespones("Contact"):
        **ทริคการแก้ตัวแปรทั้งหมดโดยไม่นี่งลบทีละตัว 1.กดคุมดำ,ไฮไลท์ตัวแปรที่ผิดจากนั้นกด Ctrl+D เเล้วก็แก้ให้ถูก 
2.ทำให้มันรู้จักกันเชื่อมแอประหว่างโปรเจค โดยไปที่ Ctrl + P เเล้วกด Setting ไปที่บรรทัด install app ข้างล่างใส่ 'ชื่อแอปของเรา',
3.ไปที่เมน เช่น web_app ไปที่ urls.py ทั้งสองตัวโดย url ของแอปเเละตัวเซิฟ เเล้วไปเพิ่ม include ที่  urlเซิฟที่ข้างหลังคำว่า path
    ใต้ urlpattern ให้ใส่ต่อของเดิมว่า path('', include('ชื่อแอป.urls')),ดูที่รูปการเชื่อมต่อ หากขึ้น Error เท่ากับถูกทาง
    4.จากนั้นจะimport view ตามรูปการเเสดงหน้าเว็บ


    **ใช้คำสั่ง git log --oneline เพื่อดูคำสั่งที่เราเคย commit
    ** เอาเฮดสีเหลืองจาก logoneline จากนั้นใช้คำสั่ง git reset 7d20cb5 --hard