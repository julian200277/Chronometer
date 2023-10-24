
class Estilos_1():
    def __init__(self):
        self.estiloPrincipal = """
            QMainWindow{
                background-image: url(img/background.jpg);
             }
             QLCDNumber{
                background-color: rgba(0, 0, 2, 0.3);
                border: 2px solid black;
                margin: 4px;
                padding: 4px;
                border-radius: 20px;
                color: red;
             }
             
             QSpinBox{
                color: rgb(235, 245, 215);
                font-size: 17px;
                padding: 8px;
                background: rgba(0, 0, 2, 0.3);
             }

             QPushButton{
                color: rgb(255, 255, 255);
                background-color: rgba(0, 0, 2, 0.3);
                border-radius: 15px;
                font-size: 14px;
                padding: 8px;
             }
             
            QPushButton:hover{
                background-color: rgba(245, 123, 2, 0.85);
             }
             
             QPushButton:pressed{
                background-color: rgba(255, 183, 46, 255 * 0.8);
                padding-top: 5px;
                padding-left: 9px;
                border-bottom: 1px solid rgba(0, 0, 0, 255 * 0.7);
                border-right: 1px solid rgba(0, 0, 0, 255 * 0.7);
            }

            QLabel{
                color: rgb(255, 255, 255);
                background-color: rgba(0, 0, 2, 0.0);

            }
        """


