# -*- coding: utf-8 -*-
# @Time : 2019/11/6 0:46
# @Author : wangmengmeng
import pytest
import random


class TestRerun():

    @pytest.mark.run(order=2)
    # @pytest.mark.flaky(reruns=5)
    def test_random(self):
        print(1)
        pytest.assume((random.randint(0, 4) + 3) == 5)

    @pytest.mark.run(order=3)
    def test_random2(self):
        '''
        不加mark 命令行中
        pytest -sq demo_rerun.py --reruns 5
        :return:
        '''
        print(2)
        pytest.assume((random.randint(0, 4) + 3) == 5)

    @pytest.mark.run(order=1)
    # @pytest.mark.flaky(reruns=6, reruns_delay=2)
    def test_example(self):
        print(3)
        assert random.choice([True, False])
