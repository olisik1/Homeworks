import logging

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class RunnerTest:
    def test_walk(self):
        try:
            runner = Runner('Тест', -5)
            runner.walk()
            logging.info('\\"test_walk\\" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            runner = Runner(12345, 5)
            runner.run()
            logging.info('\\"test_run\\" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')
