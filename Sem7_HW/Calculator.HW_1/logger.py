from asyncore import write
import datetime

def write_log(some_str):
    open('calculator_log.txt', 'a').write(f'{datetime.datetime.today()}; {some_str} \n')

    # Логирование в файл


  #  def log_to_file(temp, result):
       # with open('Seminar_Task\log.csv', 'a') as file:
      #      file.write(f'{datetime.today()}; {temp[0]}; {temp[2]};{temp[1]};{result}; \n')