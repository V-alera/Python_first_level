
import user_interface as ui
import logger as lg
import crud



lg.logging.info('Start')
crud.initBase('phone_base.csv')
ui.ls_menu()