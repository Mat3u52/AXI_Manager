class Config:
    def __init__(self) -> None:
        """
        The config file contains the paths and settings.

        :return: settings and paths
        :rtype: None
        """
        self.title = 'AXI - Manager'
        self.screenWidth = 690
        self.screenHeight = 820
        self.bgColor = '#000000'
        #self.ico = 'img/main/25x25/axi.ico'
        #self.ico = 'img/main/25x25/axi.xbm'
        self.ico = 'img/main/25x25/axi.png'
        #self.ico = ''

        self.scrollX = 645
        self.scrollY = 27
        self.scrollHeight = 523

        self.machines = ('5DX I ( V849 )', '5DX II ( V817 )',
                         'ViTrox Ex I ( V810-3163 )', 'ViTrox Ex II ( V810-3483S2EX )',
                         'ViTrox Ex III ( V810-3553S2EX )', 'ViTrox XXL I ( V810-8120S2 )')
        self.devices = ('V810-3163', 'V810-3483S2EX', 'V810-3553S2EX', 'V810-8120S2', 'V817', 'V849')
        self.pathImgDefault = 'img/lackOfPicture/board.png'

        self.pathLog = '/root/PythonDeveloper/AXI_Manager_Source_Files/Log'
        #self.pathLog = 'C:\\_PythonProject\\AXI_Manager_Source_Files\\Log'
        self.pathRecipe = '/root/PythonDeveloper/AXI_Manager_Source_Files/images'
        # self.pathRecipe = 'C:\\_PythonProject\\AXI_Manager_Source_Files\\images'

        self.pathImg5DX1 = '/root/PythonDeveloper/AXI_Manager_Source_Files/5DX/images/V849/'
        #self.pathImg5DX1 = 'C:/_PythonProject/AXI_Manager_Source_Files/5DX/images/V849/'
        #self.pathImg5DX1 = 'Y:/5DX/images/V849/'

        self.pathImg5DX2 = '/root/PythonDeveloper/AXI_Manager_Source_Files/5DX/images/V817/'
        #self.pathImg5DX2 = 'C:/_PythonProject/AXI_Manager_Source_Files/5DX/images/V817/'
        #self.pathImg5DX2 = '5DX/images/V817/'
        #self.pathImg5DX2 = 'Y:/5DX/images/V817/'

        self.pathImgV8103163 = '/root/PythonDeveloper/AXI_Manager_Source_Files/images/V810-3163/'
        #self.pathImgV8103163 = 'C:/_PythonProject/AXI_Manager_Source_Files/images/V810-3163/'
        #self.pathImgV8103163 = 'X:/images/V810-3163/'

        self.pathImgV8103483S2EX = '/root/PythonDeveloper/AXI_Manager_Source_Files/images/V810-3483S2EX/'
        #self.pathImgV8103483S2EX = 'C:/_PythonProject/AXI_Manager_Source_Files/images/V810-3483S2EX/'
        #self.pathImgV8103483S2EX = 'X:/images/V810-3483S2EX/'

        self.pathImgV8103553S2EX = '/root/PythonDeveloper/AXI_Manager_Source_Files/images/V810-3553S2EX/'
        #self.pathImgV8103553S2EX = 'C:/_PythonProject/AXI_Manager_Source_Files/images/V810-3553S2EX/'
        #self.pathImgV8103553S2EX = 'X:/images/V810-3553S2EX/'

        self.pathImgV8108120S2 = '/root/PythonDeveloper/AXI_Manager_Source_Files/images/V810-8120S2/'
        #self.pathImgV8108120S2 = 'C:/_PythonProject/AXI_Manager_Source_Files/images/V810-8120S2/'
        #self.pathImgV8108120S2 = 'X:/images/V810-8120S2/'

