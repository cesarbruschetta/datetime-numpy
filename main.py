import re
import numpy as np
from datetime import datetime, timedelta
from calendar import monthrange


class ManagerDates:
    def date_is_valid(self, date):
        """
            função que receba uma data no formato dd/mm/YYYY e determine se a mesma é  válida. 
            A data será válida apenas se estiver no formato dd/mm/YYYY.
        """
        isValidDate = True
        try:
            day, month, year = date.split("/")
            datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        return isValidDate

    def date_weekday(self, date):
        """
           função que rebeba uma data e retorne o dia da semana correspondente. 
           Ex: "Saturday"
        """
        return date.strftime("%A")

    def convert_string_to_date(self, date_str):
        """
            função que receba uma data em formato string e retorne em formato datetime. 
            Formatos válidos: "dd/mm/YYYY", "dd-mm-YYYY" , "ddmmYYYY", 
            retorna False se a data não esta em um desses formatos.
        """
        try:
            date_str = re.sub("(\/|-)", "", date_str)
            obj_date = datetime.strptime(date_str, "%d%m%Y")
            return obj_date
        except ValueError:
            return False

    def get_all_dates(self, month, year):
        """
            função que recebe o ano e o mês e retorne todas as datas do mês. 
            Obs: utilize o Numpy (arange).
        """
        _, last_day = monthrange(int(year), int(month))
        stop_date = datetime(int(year), int(month), last_day)

        n_array = np.arange(
            start=datetime(int(year), int(month), 1),
            stop=stop_date,
            step=timedelta(days=1),
            dtype=datetime,
        )
        result = n_array.tolist()
        result.append(stop_date)
        return result

    def count_days_mounth(self, month, year):
        """
            função que recebe o ano e o mês e retorne a quantidade de dias úteis que ele possui. 
            Obs: Utilize o Numpy.
        """
        days_of_month = self.get_all_dates(month, year)
        workdays = np.is_busday(np.array(days_of_month).astype("datetime64[D]"))
        return np.count_nonzero(workdays)

    def get_first_monday(self, year):
        """
            função que recebe o ano e encontre a primeira segunda-feira de maio. 
            O retorno deve ser uma string no formato "dd/mm/YYYY". 
            Obs: Utilize NumPy.
        """
        date = np.busday_offset(
            "%s-05" % year,
            0,
            roll="forward",
            holidays=["%s-05-01" % year],
            weekmask="Mon",
        )
        return date.tolist().strftime("%d/%m/%Y")
