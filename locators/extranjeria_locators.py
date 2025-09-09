from selenium.webdriver.common.by import By


class ExtranjeriaPageLocators:
    PROVINCIAS_DISPONIBLES = (By.CSS_SELECTOR, '#form')
    COOKIES = (By.CSS_SELECTOR, '#cookie_action_close_header')
    ACCEPTAR_BUTTON = (By.CSS_SELECTOR, '#btnAceptar')

    OFICINA = (By.CSS_SELECTOR, '#sede')
    TRAMITE = (By.ID, 'tramiteGrupo[0]')

    ENTRAR = (By.CSS_SELECTOR, '#btnEntrar')

    NIE = (By.CSS_SELECTOR, '#txtIdCitado')
    NOMBRE_Y_APEDIDOS = (By.CSS_SELECTOR, '#txtDesCitado')
    PAIS = (By.CSS_SELECTOR, '#txtPaisNac')
    BTN_ACEPTAR = (By.CSS_SELECTOR, '#btnEnviar')

    SOLICITAR_CITA = (By.CSS_SELECTOR, '#btnEnviar')

    TELEFONO = (By.CSS_SELECTOR, '#txtTelefonoCitado')
    EMAIL1 = (By.CSS_SELECTOR, '#emailUNO')
    EMAIL2 = (By.CSS_SELECTOR, '#emailDOS')
    SIGUIENTE = (By.CSS_SELECTOR, '#btnSiguiente')


    moderation = (By.XPATH, "//a[@target='_blank'][contains(text(),'Модерация')]")
    unbanned = (By.XPATH, "//a[9]")
    reason = (By.ID, "response_templates_select")
    accept = (By.CSS_SELECTOR, "input[name='msg_button']")
    count_text = (By.XPATH, "//option[@value='123']")
    intim_text = (By.XPATH, "//span[contains(text(),'Рассылка рекламы')]")
    osk_text = (By.XPATH, "//span[contains(text(),'Угрозы, оскорбления')]")
    female = (By.CSS_SELECTOR, ".nameF")
    text_field = (By.CSS_SELECTOR, "#js-message")
    fast_unban = (By.XPATH, "//a[contains(text(),'разбанить')]")
    fid_number = (By.CSS_SELECTOR, "input[name='fid']")
    count_text_auto = "//option[@value='{key}']"
    image = (By.XPATH, "//div[contains(@class,'item Approved')]")
    imageneg = (By.XPATH, "//div[contains(@class,'item Rejected ')]")
    gender = (By.CSS_SELECTOR, "#optGender")
    email = (By.CSS_SELECTOR, "#txtEmail")
    ban_text = (By.CSS_SELECTOR, "div[class='col-md-4'] span")
    ban_text2 = (By.XPATH, "(//div[@class='col-md-4']//span)[2]")
    messages = (By.XPATH, "//a[contains(text(),'Сообщения')]")
    language = (By.CSS_SELECTOR, ".mto")




    all_messages = (By.XPATH, "//ul[@class='list-unstyled']")
    frame_loc = (By.XPATH, "//iframe[@id='frame']")


class ShadowDOMLocators:
    shadloc = '.no-outline::shadow #quick-show-in-folder::shadow #icon'

