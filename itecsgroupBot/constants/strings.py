class Strings:
    class Global:
        WELLCOME = "سلام به ربات شرکت آیتکس خوش آمدید!"

    class Product:
        NAME = "نام"
        PRICE = "قیمت"
        DATE = "تاریخ"
        AUTHOR = "ثبت کننده"
        CATEGORY = "دسته بندی"
        DESCRIPTION = "توضیحات"

    class UserInput:
        PRODUCT_NAME = "لطفا نام محصول را وارد نمایید"
        PRICE = "لطفا قیمت محصول را وارد نمایید"
        CATEGORY = "دسته بندی مورد نظر را انتخاب نمایید"
        DESCRIPTION = "توضیحات تکمیلی درباره محصول را وارد نمیایید"
        PRODUCT_ADDED_SUCCESSFULLY = "محصول با موفقیت ثبت شد"

    class Categories:
        CHAHAK = "چاهک"
        class CatChahack :
            MECHANIC = "مکانیک"
            class CatMechanic :
                DARB = "ریل"
                RAIL = "درب"
                BOXOL = "بکسل"
                SIMBOXOL = "سیم بکسل"
                RAHANDAZI = "راه اندازی"
                OVERLOAD = "اورلود"
                BUFFER = "بافر"
                KABIN = "کابین"
                NIME = "نیمه"
                TAMAM = "تمام"

        class CatMotorKhane :
            MOTOR_KHANE = "موتورخانه"
            class CatTabloFarman :
                TABLO_FARMAN = "تابلو فرمان"
                GEARBOX = "گیربکس"
                GEARLESS = "گیرلس"
                MOTOR = "موتور"
                MOTEALEGHAT = "متعلقات"
                FALAKE_HARZ_GERD = "فلکه هرزگرد"
                GAVERNER = "گاورنر"
                TABLO_SE_FAZ = "تابلو سه فاز"


    class Error:
        INVALID_INPUT = "لطفا قیمت را به عدد وارد نمایید"
