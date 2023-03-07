__author__ = 'Administrator'

import configparser


class DoConfig:
    @staticmethod
    def read_config(file_name, section, option):
        """——————从配置文件读取配置————
            参数：
                file_name：配置文件路径  str；  section：模块名  str； option：参数名  str；
            返回：   option在配置文件中对应的值  ；  str
            ————————————————————————————————————————"""
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8")
        return cf.get(section, option)

    @staticmethod
    def set_config(file_name, option, value):
        """————————修改配置文件中参数的值————————
            参数：
                file_name：配置文件路径  str；  option：参数名  str； value：修改值  str；
            ————————————————————————————————————————"""
        with open(file_name, 'r', encoding='utf-8') as old_config:
            lines = old_config.readlines()
            f_len = len(lines)
            for i in range(f_len):
                if lines[i].startswith(option):
                    config_value = lines[i].split('=')
                    lines[i] = config_value[0] + '=' + str(value) + '\n'
                    break
                else:
                    continue
        with open(file_name, 'w', encoding='utf-8') as new_config:
            new_config.writelines(lines)


