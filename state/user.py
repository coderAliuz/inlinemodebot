from aiogram.dispatcher.filters.state import StatesGroup,State

class UserState(StatesGroup):
    fullname=State()
    phone=State()
    check=State()
    
class MainState(StatesGroup):
    main=State()
    edituser=State()
    editfullname=State()
    editphone=State()
    deleteuser=State()
