from peppi import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from examination_paper import *


class MainWindow(QMainWindow, Ui_MainWindow):
    __style_active = '''
            QPushButton
    {
    	background-color: rgb(88, 146, 203);
    	color: rgb(255, 255, 255);
    	font-family:Microsoft Yahei;
    	font-size:15pt;
    }
    QPushButton:hover
    {

    	background-color: rgb(18, 123, 191);
    }
    QPushButton:pressed
    {
    	background-color: rgb(88, 146, 203);
        padding-left:3px;
        padding-top:3px;
    }
        '''
    __style_deactive = '''
                QPushButton
    {
    	background-color: rgb(88, 146, 203);
    	color: rgb(255, 255, 255);
    	font-family:Microsoft Yahei;
    	font-size:15pt;
    }
        '''

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.__paper = None
        self.content_dict = self.__get_content()
        self.btn_generate.clicked.connect(self.__load_paper)
        self.btn_submit.clicked.connect(self.__submit)
        a=QtWidgets.QGroupBox()
        a.show()
        self.btn_check.clicked.connect(self.__show_right_answer)


    def __get_content(self):
        question_frames = [self.wd_content.children()[i] for i in range(1, 11)]
        question_dic = {"pic": [], "ques": [], "input": [], "asw": []}
        for q in question_frames:
            question_dic["pic"].append(q.children()[1])
            question_dic["ques"].append(q.children()[2])
            question_dic["input"].append(q.children()[3])
            question_dic["asw"].append(q.children()[4])
        return question_dic

    def __set_active_show_answer(self, is_enable):
        self.btn_check.setEnabled(is_enable)
        if is_enable:
            self.btn_check.setStyleSheet(self.__style_active)
        else:
            self.btn_check.setStyleSheet(self.__style_deactive)

    def __load_paper(self):
        self.__paper = ExaminationPaper()
        for i in range(0, 10):
            self.content_dict["pic"][i].setStyleSheet("")
            self.content_dict["ques"][i].setText(str(self.__paper.questions[i]))
            self.content_dict["input"][i].setText("")
            self.content_dict["asw"][i].setText("")
        self.__set_active_show_answer(False)

    def __fill_peppi(self):
        for i in range(10):
            if self.content_dict["input"][i].text() == str(self.__paper.questions[i].answer):
                self.content_dict["pic"][i].setStyleSheet("background-image: url(img/happy.png)")
            else:
                self.content_dict["pic"][i].setStyleSheet("background-image: url(img/sad.png)")

    def __write_file(self, content):
        with open("Exam_puple2020.txt", mode="a", encoding='utf-8')as f:
            f.write(content)

    def __submit(self):
        if self.__paper is None:
            QtWidgets.QMessageBox.information(self.btn_submit, "Oops", "请先生成试题再提交")
        else:
            self.__set_active_show_answer(True)
            self.__paper.student_name = self.ed_name.text()
            self.__paper.student_info = self.ed_class.text()
            self.__paper.check([self.content_dict["input"][i].text() for i in range(10)])
            self.__fill_peppi()
            QtWidgets.QMessageBox.information(self.btn_submit, "成绩公布", str(self.__paper.grades) + " 分\n加油！")
            self.__write_file(str(self.__paper))

    def __show_right_answer(self):
        for i in range(10):
            self.content_dict["asw"][i].setText(str(self.__paper.questions[i].answer))


