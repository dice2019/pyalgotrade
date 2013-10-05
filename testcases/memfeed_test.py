# PyAlgoTrade
# 
# Copyright 2013 Gabriel Martin Becedillas Ruiz
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#	http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: Gabriel Martin Becedillas Ruiz <gabriel.becedillas@gmail.com>
"""

import unittest
import datetime

from pyalgotrade.feed import memfeed
from pyalgotrade import observer
import feed_test

class MemFeedTestCase(unittest.TestCase):
	def testBaseFeedInterface(self):
		values = [(datetime.datetime.now() + datetime.timedelta(seconds=i), {"i":i}) for i in xrange(100)]
		feed = memfeed.MemFeed()
		feed.addValues(values)
		feed_test.testBaseFeedInterface(self, feed)

	def testFeed(self):
		values = [(datetime.datetime.now() + datetime.timedelta(seconds=i), {"i":i}) for i in xrange(100)]

		feed = memfeed.MemFeed()
		feed.addValues(values)

		# Check that the dataseries are available after adding values.
		self.assertTrue("i" in feed)
		self.assertEquals(len(feed["i"]), 0)
		self.assertFalse("dt" in feed)

		dispatcher = observer.Dispatcher()
		dispatcher.addSubject(feed)
		dispatcher.run()

		self.assertTrue("i" in feed)
		self.assertFalse("dt" in feed)
		self.assertEquals(feed["i"][0], 0)
		self.assertEquals(feed["i"][-1], 99)

def getTestCases():
	ret = []

	ret.append(MemFeedTestCase("testBaseFeedInterface"))
	ret.append(MemFeedTestCase("testFeed"))

	return ret

