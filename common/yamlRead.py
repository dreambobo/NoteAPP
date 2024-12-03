import yaml

from main import DIR, ENVIRON


class YamlRead():
    # @staticmethod
    def env_config(self):
        with open(file=f'{DIR}/business_common/data/env_config/{ENVIRON}/config.yml', mode='r', encoding='utf-8') as f:
            return yaml.load(f,Loader=yaml.FullLoader)

    # @staticmethod
    def data_config(self):
        with open(file=f'{DIR}/business_common/data/api_config/api.yml', mode='r', encoding='utf-8') as f:
            return yaml.load(f,Loader=yaml.FullLoader)


if __name__ == '__main__':
    print(YamlRead().data_config()['group_create'])
