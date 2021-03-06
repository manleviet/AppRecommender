#!/usr/bin/env python
"""
    recommenderTests - Recommender class test case
"""
__author__ = "Tassia Camoes Araujo <tassia@gmail.com>"
__copyright__ = "Copyright (C) 2011 Tassia Camoes Araujo"
__license__ = """
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import unittest2
import sys
sys.path.insert(0,'../')
from recommender import RecommendationResult, Recommender
from user import User
from config import Config
from strategy import ContentBasedStrategy, CollaborativeStrategy

class RecommendationResultTests(unittest2.TestCase):
    @classmethod
    def setUpClass(self):
        self.result = RecommendationResult({"gimp":1.5,"inkscape":3.0,"eog":1})

    def test_str(self):
        string = "\n 0: inkscape\n 1: gimp\n 2: eog\n"
        self.assertEqual(self.result.__str__(),string)

    def test_get_prediction(self):
        prediction = [("inkscape",3.0),("gimp",1.5),("eog",1)]
        self.assertEqual(self.result.get_prediction(),prediction)

class RecommenderTests(unittest2.TestCase):
    @classmethod
    def setUpClass(self):
        cfg = Config()
        cfg.popcon_index = "test_data/.sample_pxi"
        cfg.popcon_dir = "test_data/popcon_dir"
        cfg.clusters_dir = "test_data/clusters_dir"
        self.rec = Recommender(cfg)

    def test_set_strategy(self):
        self.rec.set_strategy("cb")
        self.assertIsInstance(self.rec.strategy,ContentBasedStrategy)
        self.assertEqual(self.rec.strategy.content,"full")
        self.rec.set_strategy("cbt")
        self.assertIsInstance(self.rec.strategy,ContentBasedStrategy)
        self.assertEqual(self.rec.strategy.content,"tag")
        self.rec.set_strategy("cbd")
        self.assertIsInstance(self.rec.strategy,ContentBasedStrategy)
        self.assertEqual(self.rec.strategy.content,"desc")
        self.rec.set_strategy("col")
        self.assertIsInstance(self.rec.strategy,CollaborativeStrategy)

    def test_get_recommendation(self):
        user = User({"inkscape": 1, "gimp": 1, "eog":1})
        result = self.rec.get_recommendation(user)
        self.assertIsInstance(result, RecommendationResult)
        self.assertGreater(len(result.item_score),0)

if __name__ == '__main__':
        unittest2.main()
