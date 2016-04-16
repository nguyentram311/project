from flask import Flask, render_template
# from bs4 import  BeautifulSoup
# import requests
# import re
article_1 = {
    "title" : "Project Escher: dự án phát triển hệ thống in 3D đa đầu của Autodesk",
    "image" : "https://tinhte.cdnforo.com/store/2016/03/3647733_cv-Escher_tinhte.gif",
    "content": "Một chiếc máy in 3D giá cả vừa phải cũng đi kèm với một hạn chế: chúng thường nhỏ và chỉ có thể in ra các sản phẩm có kích thước nhỏ. Để tạo ra thứ gì đó lớn hơn, người dùng cần phải chia nhỏ thiết kế của họ ra, sau đó lắp ghép lại. Tuy nhiên, Autodesk đưa ra một cách tiếp cận hiệu quả hơn: tạo ra một hệ thống in đa đầu, giúp cho việc sản xuất các bộ phận cỡ lớn trở nên nhanh chóng và dễ dàng. Nằm trong dự án mới Project Escher, Autodesk muốn thiết lập một ‘dây chuyền in 3D’, với các đầu in...",
    "author" : "tieumichanhche"
}

article_2 = {
    "title" : "[QC] HP Pavilion 14/15: Bạn đồng hành không thể thiếu của dân văn phòng",
    "image" : "https://tinhte.cdnforo.com/store/2016/03/3647581_CV.png",
    "content": "Khác với dân đồ họa hay game thủ, nhân viên văn phòng thường chọn “bạn đồng hành” trong suốt 8 tiếng làm việc căng thẳng mỗi ngày là một chiếc laptop đáp ứng được những tiêu chuẩn riêng phù hợp với tính chất công việc của họ. Nếu bạn vẫn chưa tìm được sản phẩm ưng ý, hãy thử “làm quen” với bộ đôi HP Pavilion 14/15 đang rất được giới văn phòng ưa chuộng. Thiết kế giúp bạn tạo dựng phong cách chuyên nghiệp Nếu như dân đồ họa hay game thủ không quan tâm đến thiết kế của một chiếc laptop...",
    "author": "Trung Dt"
}

article_3 = {
    "title" : "[BMS 2016] Toyota Fortuner 2016: thiết kế mới, nội thất sang hơn, nâng cao độ an toàn",
    "image" : "https://tinhte.cdnforo.com/store/2016/03/3647942_CV_Fortuner_2016_BMS_xe_tinhte_1.jpg",
    "content": "Fortuner 2016 là mẫu xe SUV 7 chỗ được Toyota làm mới từ diện mạo bên ngoài cho đến nội thất bên trong. Sự cải tiến của Fortuner mới sẽ giúp cho Toyota có thể cạnh tranh tốt hơn với các đối thủ như Ford Everest 2015, Mitsubishi Pajero Sport 2016… Tại Thái Lan, Toyota bổ sung thêm 4 phiên bản TRD Sportivo, tổng cộng xe có 9 phiên bản với 3 loại động cơ khác nhau, tuỳ chọn dẫn động 2WD hoặc 4WD. Thiết kế của Fortuner 2016 gây ấn tượng mạnh...",
    "author": "TTKM"
}

List_article = [article_1,article_2,article_3]


class Article:
    def __init__(self,title,image, content, author):
         self.title=title
         self.image=image
         self.content=content
         self.author=author


List_object=[Article(article_1['title'],article_1['image'],article_1['content'],article_1['author']),
        Article(article_2['title'],article_2['image'],article_2['content'],article_2['author']),
        Article(article_3['title'],article_3['image'],article_3['content'],article_3['author'])]











app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

#bài 1
# @app.route('/index')
# def index():
#     return render_template('index.html',article=List_object[0])

#bài 2
#dùng for list ở html ko cần dùng ở hàm def nữa
@app.route('/index')
def index():
    return render_template('index2.html',htmt_list=List_object)
if __name__ == '__main__':
    app.run()


#dùng for list ở html ko cần dùng ở hàm def nữa
