from pytube import YouTube
from PyQt5 import QtWidgets, QtGui
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Video Downloader")
        self.setMaximumSize(670, 330)
        self.setMinimumSize(670, 330)
        self.setStyleSheet("background-color: white;")
        self.setWindowIcon(QtGui.QIcon("photo/800px-YouTube_social_white_squircle.svg.png"))
        self.init_ui()
        self.show()

    def init_ui(self):
        photo1 = QtWidgets.QLabel()
        photo1.setPixmap(QtGui.QPixmap("photo/11.png"))
        hBox1 = QtWidgets.QHBoxLayout()
        hBox1.addStretch()
        hBox1.addWidget(photo1)
        vBox1 = QtWidgets.QVBoxLayout()
        vBox1.addLayout(hBox1)
        vBox1.addStretch()

        label1 = QtWidgets.QLabel("YouTube Link: ")
        label1.setFont(QtGui.QFont("Arial", 16))
        self.input = QtWidgets.QLineEdit()
        self.input.setFont(QtGui.QFont("Arial", 16))

        hBox2 = QtWidgets.QHBoxLayout()
        hBox2.addWidget(label1)
        hBox2.addWidget(self.input)
        vBox2 = QtWidgets.QVBoxLayout()
        vBox2.addLayout(hBox2)
        hBox3 = QtWidgets.QHBoxLayout()

        self.video_info = QtWidgets.QLabel()
        self.video_info.setFont(QtGui.QFont("Arial", 10))
        self.button = QtWidgets.QPushButton("Download")
        self.button.setFont(QtGui.QFont("Arial", 13))
        self.info_button = QtWidgets.QPushButton("Information")
        self.info_button.setFont(QtGui.QFont("Arial", 13))
        hBox3.addWidget(self.video_info)
        hBox3.addStretch()
        hBox3.addWidget(self.info_button)
        hBox3.addWidget(self.button)
        vBox2.addLayout(hBox3)
        vBox2.addStretch()

        self.comboBox = QtWidgets.QComboBox()
        qualities = ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p"]
        self.comboBox.addItems(qualities)
        self.comboBox.setFont(QtGui.QFont("Arial", 13))
        hBox5 = QtWidgets.QHBoxLayout()
        hBox5.addStretch()
        hBox5.addWidget(self.comboBox)


        photo2 = QtWidgets.QLabel()
        photo2.setPixmap(QtGui.QPixmap("photo/800px-YouTube_social_white_squircle.svg.png"))
        self.info = QtWidgets.QLabel()
        self.info.setFont(QtGui.QFont("Arial", 13))
        hBox4 = QtWidgets.QHBoxLayout()
        hBox4.addWidget(self.info)
        hBox4.addStretch()
        hBox4.addWidget(photo2)


        vBox = QtWidgets.QVBoxLayout()
        vBox.addLayout(vBox1)
        vBox.addLayout(vBox2)
        vBox.addLayout(hBox5)
        vBox.addStretch()
        vBox.addLayout(hBox4)
        self.setLayout(vBox)

        self.info_button.clicked.connect(self.about_video)
        self.button.clicked.connect(self.download)


    def about_video(self):
        try:
            Link = str(self.input.text())
            video = YouTube(Link)
            self.info.setText(" ")
            self.video_info.setStyleSheet("color: blue;")
            self.video_info.setText("Title: {}\nNumber of views: {}\nLength of video: {} sec\n"
                                    "Author: {}\nAge Restricted: {}".format(video.title, video.views, video.length,
                                                                            video.author, video.age_restricted))
        except:
            self.video_info.setText(" ")
            self.info.setStyleSheet("color: red;")
            self.info.setText("YouTube link was wrong!")

    def download(self):
        try:
            Link = self.input.text()
            video = YouTube(Link)
            quality = str(self.comboBox.currentText())
            video.streams.filter(res=quality, file_extension='mp4').first().download("C:/Users/User/Downloads")
            #stream = video.streams.get_highest_resolution()
            #stream.download("C:/Users/User/Downloads")
            self.info.setStyleSheet("color: green;")
            self.info.setText("Video Downloaded. Check your Downloads folder.")

        except:
            self.video_info.setText(" ")
            self.info.setText("Error!")
            self.info.setStyleSheet("color: red;")


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
